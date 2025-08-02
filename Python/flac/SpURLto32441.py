import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import asyncio
import os
import glob
import zipfile
import time
import requests
import shutil

from applescript import AppleScript
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

async def spotify_to_tidal_deezer(spotify_url):
    api_url = f"https://api.song.link/v1-alpha.1/links"
    params = {"url": spotify_url}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        tidal_info = data.get("linksByPlatform", {}).get("tidal")
        deezer_info = data.get("linksByPlatform", {}).get("deezer")
        if tidal_info: return ("TIDAL", tidal_info.get("url"))
        if deezer_info: return ("Deezer", deezer_info.get("url"))
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

async def close_all_chrome():
    AppleScript('''
                    if application "Google Chrome" is running then
                        tell application "Google Chrome" to quit
                    end if
                ''').run()

async def download_tidal(tidal_deezer):
    platform, url = tidal_deezer
    await close_all_chrome()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    download_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))
    os.makedirs(download_dir, exist_ok=True)
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # No prompt
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    async with webdriver.Chrome(options=options) as driver:
        await driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": download_dir,
        })
        await driver.get('https://us.doubledouble.top/', wait_load=True)
        while True:
            try: url_input = await driver.find_element(By.ID, 'dl-input', timeout=1); break
            except Exception: await asyncio.sleep(0.1)
        # await driver.execute_script('arguments[0].value = arguments[1];', url_input, tidal_url)
        await url_input.send_keys(url)
        while True:
            try: external_checkbox = await driver.find_element(By.ID, 'external', timeout=1); break
            except Exception: await asyncio.sleep(0.1)
        await external_checkbox.click()
        while True:
            try: dl_button = await driver.find_element(By.ID, 'dl-button', timeout=1); break
            except Exception: await asyncio.sleep(0.1)
        await dl_button.click()
        
        print("Generating .crdownload")
        while True:
            crdownload_files = glob.glob(os.path.join(download_dir, "*.crdownload"))
            if not crdownload_files: time.sleep(1); continue
            else: break

        if platform == "TIDAL": print("Downloading from TIDAL")
        elif platform == "Deezer": print("Downloading from Deezer")
        while True:
            files = glob.glob(os.path.join(download_dir, "*.zip")) + glob.glob(os.path.join(download_dir, "*.flac"))
            if not files: time.sleep(1); continue
            else: break

        return files[0] if files else None


async def extract_flac_lrc(downloaded_file):
    # temp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))
    done_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'done'))
    file_path = downloaded_file
    filename = os.path.basename(downloaded_file)
    os.makedirs(done_dir, exist_ok=True)
    
    if filename.lower().endswith('.flac'):
        try:
            destination = os.path.join(done_dir, filename)
            shutil.move(file_path, destination)
            print(f"Moved FLAC file: {filename}")
            return
        except Exception as e:
            print(f"Error moving FLAC file {filename}: {e}")
            return
    
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            extracted_files = []

            flac_files = [f for f in file_list if f.lower().endswith('.flac')]
            for flac_file in flac_files:
                try:
                    zip_ref.extract(flac_file, done_dir)
                    extracted_files.append(flac_file)
                    print(f"Extracted FLAC: {flac_file}")
                except Exception as e:
                    print(f"Error extracting FLAC {flac_file}: {e}")
            
            lrc_files = [f for f in file_list if f.lower().endswith('.lrc')]
            for lrc_file in lrc_files:
                try:
                    zip_ref.extract(lrc_file, done_dir)
                    extracted_files.append(lrc_file)
                    print(f"Extracted LRC: {lrc_file}")
                except Exception as e:
                    print(f"Error extracting LRC {lrc_file}: {e}")
            
            os.remove(file_path)
            
    except zipfile.BadZipFile:
        print(f"Error: {filename} is not a valid zip file")
    except Exception as e:
        print(f"Error extracting zip file: {e}")
    
async def main(spotify_url):
    tidal_deezer = await spotify_to_tidal_deezer(spotify_url)
    if not tidal_deezer: print("Tidal/Deezer URL not found."); return

    downloaded_file = await download_tidal(tidal_deezer)
    if not downloaded_file: print("No file downloaded"); return

    await extract_flac_lrc(downloaded_file)

if __name__ == '__main__':
    url = input("Input with URL: ")
    asyncio.run(main(url))