import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import asyncio
import os
import json
import glob
import zipfile
# import time
import requests
import shutil
import re
import httpx

from applescript import AppleScript
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

services = ["tidal", "deezer", "apple music", "amazon music"]

def create_spotify_client():
    client_secrets_path = os.path.join(os.path.expanduser("~"), ".Spotify_client_secrets.json")
    with open(client_secrets_path) as f:
        client_secrets = json.load(f)
    auth_manager = SpotifyClientCredentials(client_id=client_secrets["client_id"], client_secret=client_secrets["client_secret"])
    return spotipy.Spotify(auth_manager=auth_manager)

def extract_spotify_track_urls(url):
    spotify = create_spotify_client()

    if "album" in url:
        match = re.search(r'album/([a-zA-Z0-9]+)', url)
        if not match:
            return []
        album_id = match.group(1)
        results = spotify.album_tracks(album_id)
        tracks = results['items']
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])
        return [track['external_urls']['spotify'] for track in tracks]

    elif "playlist" in url:
        match = re.search(r'playlist/([a-zA-Z0-9]+)', url)
        if not match:
            return []
        playlist_id = match.group(1)
        results = spotify.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])
        return [track['track']['external_urls']['spotify'] for track in tracks if track['track']]

    else:
        return [url] if re.match(r'https?://open\.spotify\.com/track/[a-zA-Z0-9]+', url) else []


async def spotify_to_HiRes(spotify_url):
    track_platforms = []  # List of tuples: (spotify_url, [(platform, url), ...])

    spotify_urls = extract_spotify_track_urls(spotify_url)
    for i, spotify_track_url in enumerate(spotify_urls, 1):
        api_url = f"https://api.song.link/v1-alpha.1/links"
        params = {"url": spotify_track_url}

        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 429:
                print("API rate limit reached. Waiting 60 seconds...")
                await asyncio.sleep(60)
                response = requests.get(api_url, params=params)
            
            response.raise_for_status()
            data = response.json()
            
            # Collect all available platforms for this track
            platforms_for_track = []
            for service in services:
                service_info = data.get("linksByPlatform", {}).get(service)
                if service_info: 
                    platforms_for_track.append((service.capitalize(), service_info.get("url")))
            
            if platforms_for_track:
                track_platforms.append((spotify_track_url, platforms_for_track))
            else:
                print(f"No platforms found for track {i}: {spotify_track_url}")
                
        except Exception as e:
            print(f"Error getting platforms for track {i}: {e}")
    
    print(f"Found {len(track_platforms)} tracks with available platforms")
    return track_platforms if track_platforms else None

async def close_all_chrome():
    AppleScript('''
                    if application "Google Chrome" is running then
                        tell application "Google Chrome" to quit
                    end if
                ''').run()

async def check_services():
    """
    Check which music services are currently working by making a GET request to the server stats API.
    Returns a list of service names that are currently working.
    """
    service_ids = ["tidal", "deezer", "apple", "amznmusic"]
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get("https://us.doubledouble.top/server-stats/")
            
            if response.status_code == 200:
                data = response.json()
                status_info = data.get("status", {})
                
                working_services = []
                for service_name, service_data in status_info.items():
                    if service_name in service_ids:
                        if service_data.get("working", False):
                            working_services.append(services[service_ids.index(service_name)])
                            # print(f"✅ {service_name.capitalize()} is working")
                        # else:
                            # print(f"❌ {service_name.capitalize()} is not working")
                
                # print(f"Total working services: {len(working_services)}")
                return working_services
            else:
                print(f"Failed to get server stats. Status code: {response.status_code}")
                return []
                
    except Exception as e:
        print(f"Error checking service status: {e}")
        return []


async def download_HiRes(track_platforms):
    await close_all_chrome()

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    download_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))
    os.makedirs(download_dir, exist_ok=True)
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    async with webdriver.Chrome(options=options) as driver:
        await driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": download_dir,
        })
        # downloaded_files = []
        await driver.get('https://us.doubledouble.top/', wait_load=True)
        while True:
            try: external_checkbox = await driver.find_element(By.ID, 'external', timeout=1); break
            except Exception: await asyncio.sleep(0.1)
        await external_checkbox.click()

        for track_index, (spotify_url, platforms) in enumerate(track_platforms, 1):
            print(f"Processing track {track_index}/{len(track_platforms)}")
            track_downloaded = False

            online_services = await check_services()
            for platform, url in platforms:
                if platform.lower() not in online_services:
                    print(f"{platform} is not available, skipping...")
                    continue
                if track_downloaded: break

                while True:
                    try: url_input = await driver.find_element(By.ID, 'dl-input', timeout=1); break
                    except Exception: await asyncio.sleep(0.1)
                await url_input.clear()
                await url_input.send_keys(url)
                while True:
                    try: dl_button = await driver.find_element(By.ID, 'dl-button', timeout=1); break
                    except Exception: await asyncio.sleep(0.1)
                await dl_button.click()

                print(f"Downloading from {platform}: ", end='')
                while True:
                    files = glob.glob(os.path.join(download_dir, "*.zip")) + glob.glob(os.path.join(download_dir, "*.flac")) + glob.glob(os.path.join(download_dir, "*.m4a"))
                    if files: break
                    await asyncio.sleep(1)

                if files:
                    # downloaded_files.append(files[0])
                    print(f"Successfully downloaded: {os.path.basename(files[0])}")
                    await extract_flac_lrc(files[0], platform)
                    track_downloaded = True
                else:
                    print(f"No file downloaded from {platform}, trying next platform...")
            
            if not track_downloaded:
                print(f"Failed to download track {track_index} from any platform")

async def extract_flac_lrc(downloaded_file, platform):
    done_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'done'))
    
    # Create platform-specific subdirectory
    platform_dir = os.path.join(done_dir, platform.replace(' ', '_').lower())
    os.makedirs(platform_dir, exist_ok=True)
    
    file_path = downloaded_file
    filename = os.path.basename(downloaded_file)
    
    if filename.lower().endswith('.flac'):
        try:
            destination = os.path.join(platform_dir, filename)
            shutil.move(file_path, destination)
            print(f"Extracted: {filename} to {platform} folder")
            return
        except Exception as e:
            print(f"Error moving FLAC file {filename}: {e}")
            return
    elif filename.lower().endswith('.m4a'):
        try:
            destination = os.path.join(platform_dir, filename)
            shutil.move(file_path, destination)
            print(f"Extracted: {filename} to {platform} folder")
            return
        except Exception as e:
            print(f"Error moving M4A file {filename}: {e}")
            return

    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            extracted_files = []

            flac_files = [f for f in file_list if f.lower().endswith('.flac')]
            for flac_file in flac_files:
                try:
                    zip_ref.extract(flac_file, platform_dir)
                    extracted_files.append(flac_file)
                    print(f"Extracted: {flac_file} to {platform} folder")
                except Exception as e:
                    print(f"Error extracting FLAC {flac_file}: {e}")
            
            lrc_files = [f for f in file_list if f.lower().endswith('.lrc')]
            for lrc_file in lrc_files:
                try:
                    zip_ref.extract(lrc_file, platform_dir)
                    extracted_files.append(lrc_file)
                    print(f"Extracted: {lrc_file} to {platform} folder")
                except Exception as e:
                    print(f"Error extracting LRC {lrc_file}: {e}")
            
            os.remove(file_path)
            
    except zipfile.BadZipFile:
        print(f"Error: {filename} is not a valid zip file")
    except Exception as e:
        print(f"Error extracting zip file: {e}")
    
async def main(spotify_url):
    track_platforms = await spotify_to_HiRes(spotify_url)
    if not track_platforms: print("No tracks with available platforms found."); return

    await download_HiRes(track_platforms)

if __name__ == '__main__':
    url = input("Input with URL: ")
    asyncio.run(main(url))
