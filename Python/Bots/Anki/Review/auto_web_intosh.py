import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import os

# os.environ.pop("http_proxy", None)
# os.environ.pop("https_proxy", None)
# os.environ.pop("all_proxy", None)
# os.environ["no_proxy"] = "127.0.0.1,localhost"

import time
import random
import asyncio
# import subprocess
from datetime import datetime, timedelta

from selenium_driverless import webdriver
from selenium_driverless.types.by import By

from applescript import AppleScript
from pync import Notifier

email_prefix = "hsiaoseanhs"
bir = 911119
remain = -1

def notify(message, title="Anki Automation"):
    """Send notification and track its ID"""
    try:
        # Remove previous notifications first
        Notifier.remove()
        # Send new notification
        Notifier.notify(message, title=title)
    except Exception as e:
        print(f"Notification error: {e}")

# async def close_all_chrome():
#     try: os.system('taskkill /F /IM "chrome.exe"') # Windows
#     except: pass
async def close_all_chrome():
    # try:
    #     # Kill all selenium-driverless Chrome processes
    #     os.system('pkill -f "selenium_driverless" 2>/dev/null')
    #     os.system('pkill -f "Google Chrome.*remote-debugging-port" 2>/dev/null')
        
    #     # Also try AppleScript for any regular Chrome instances
    # AppleScript('''
    #                 if application "Google Chrome" is running then
    #                     tell application "Google Chrome" to quit
    #                 end if
    #             ''').run()
    os.system('''
                if pgrep "Google Chrome" > /dev/null; then
                    killall "Google Chrome"
                fi
              ''')
        # # Wait a moment for processes to terminate
        # await asyncio.sleep(2)
        
        # # Clean up selenium-driverless cache directory
        # selenium_cache_dir = os.path.expanduser('~/Library/Application Support/selenium-driverless')
        # if os.path.exists(selenium_cache_dir):
        #     try:
        #         import shutil
        #         shutil.rmtree(selenium_cache_dir)
        #         # print("Cleaned selenium-driverless cache directory")
        #     except Exception as e:
        #         print(f"Warning: Could not clean cache directory: {e}")
        #         Notifier.notify(f"Could not clean cache directory: {e}", title="Anki Automation")
        #         # notify("Anki Automation", f"Could not clean cache directory: {e}")

        # # Recreate the directory to avoid FileNotFoundError
        # try:
        #     os.makedirs(selenium_cache_dir, exist_ok=True)
        # except Exception as e:
        #     print(f"Warning: Could not recreate cache directory: {e}")
        #     Notifier.notify(f"Could not recreate cache directory: {e}", title="Anki Automation")
        #     # notify("Anki Automation", f"Could not recreate cache directory: {e}")

        # # Clean up any leftover selenium temp directories
        # os.system('rm -rf /tmp/selenium_driverless_* 2>/dev/null')
        # os.system('rm -rf /var/folders/*/T/selenium_driverless_* 2>/dev/null')
        
        # # Force garbage collection to free up resources
    import gc
    gc.collect()
        
    # except Exception as e:
    #     print(f"Warning: Error closing Chrome processes: {e}")
    #     Notifier.notify(f"Error closing Chrome processes: {e}", title="Anki Automation")
    #     # notify("Anki Automation", f"Error closing Chrome processes: {e}")
    #     pass

async def login(driver):
    await driver.get("https://ankiweb.net/account/login", wait_load=True)
    while True:
        try: Login = await driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg", timeout=1); break
        except: await driver.sleep(1)

    svelte = await driver.find_elements(By.CLASS_NAME, "form-control svelte-1ak1s42")
    await svelte[0].send_keys(email_prefix + "@gmail.com")
    await svelte[1].send_keys("sean" + str(bir))
    await Login.click()

async def practice(driver, target):
    while True:
        try:
            element = await driver.find_element(By.XPATH, "//*[text()='(02)English']", timeout=1)
            await element.click()
            break
        # except Exception as e: print("Study page:", e); await driver.sleep(1)
        except: await driver.sleep(1)
    
    count = target
    while count > 0:
        try:
            element = await driver.find_element(By.XPATH, "//*[text()='Show Answer']", timeout=1)
            await element.click()
            await driver.sleep(random.randint(50,60))
            while True:
                try:
                    btn = await driver.find_elements(By.CLASS_NAME, "btn btn-primary btn-lg m-1", timeout=1)
                    if len(btn) == 4: 
                        remain = await driver.find_element(By.CSS_SELECTOR, 'div.float-end')
                        remain = await remain.text
                        remain = remain.replace("\n", "")
                        goodtime = await driver.find_element(By.XPATH, '//*[@id="ansarea"]/div/div[3]/div')
                        goodtime = await goodtime.text
                        if goodtime == "10m":
                            await btn[2].click()
                            print(f"G 10m({remain}){count}")
                            # Notifier.notify(f"G 10m({remain}){count}", title="Anki Automation")
                            notify(f"G 10m({remain}){count}")
                            # notify("Anki Automation", f"G 10m({remain}){count}")
                        elif goodtime == "01d":
                            await btn[2].click()
                            print(f"G 01d({remain}){count}")
                            # Notifier.notify(f"G 01d({remain}){count}", title="Anki Automation")
                            notify(f"G 01d({remain}){count}")
                            # notify("Anki Automation", f"G 01d({remain}){count}")
                        else:
                            R = random.random()
                            if R <= 0.3:
                                await btn[2].click()
                                print(f"G ran({remain}){count}")
                                # Notifier.notify(f"G ran({remain}){count}", title="Anki Automation")
                                notify(f"G ran({remain}){count}")
                                # notify("Anki Automation", f"G ran({remain}){count}")
                            elif R <= 0.6:
                                await btn[1].click()
                                print(f"H ran({remain}){count}")
                                # Notifier.notify(f"H ran({remain}){count}", title="Anki Automation")
                                notify(f"H ran({remain}){count}")
                                # notify("Anki Automation", f"H ran({remain}){count}")
                            else:
                                await btn[0].click()
                                print(f"A ran({remain}){count}")
                                # Notifier.notify(f"A ran({remain}){count}", title="Anki Automation")
                                notify(f"A ran({remain}){count}")
                                # notify("Anki Automation", f"A ran({remain}){count}")
                        count -= 1
                        break
                # except Exception as e: print("btn:", e); await driver.sleep(1)
                except: await driver.sleep(1)
        # except Exception as e: print("Ans loop:", e); await driver.sleep(1)
        except: await driver.sleep(1)

async def AnkiWeb(test):
    # Increase file descriptor limit to prevent "too many open files" error
    # try:
    #     import resource
    #     soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    #     print(f"Current file descriptor limits: soft={soft}, hard={hard}")
    #     # Try to increase the soft limit to the hard limit
    #     resource.setrlimit(resource.RLIMIT_NOFILE, (min(hard, 8192), hard))
    #     new_soft, _ = resource.getrlimit(resource.RLIMIT_NOFILE)
    #     print(f"New soft limit: {new_soft}")
    # except Exception as e:
    #     print(f"Warning: Could not increase file descriptor limit: {e}")
    
    await close_all_chrome()
    if test:
        random_wait, random_Q = 0, 5
    else:
        random_wait, random_Q = random.randint(12, 34567), random.randint(20, 60)
    if random_wait <= (datetime.now() - datetime.combine(datetime.now().date(), datetime.strptime("12:00", "%H:%M").time())).total_seconds(): random_wait = 0
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    options.add_argument("--headless")
    # options.add_argument("--remote-debugging-port=6969")
    # options.add_argument("--user-data-dir=/tmp/chrome-profile")
    # options.add_argument("--no-proxy-server")
    # options.add_argument("--proxy-server='direct://'")
    # options.add_argument("--proxy-bypass-list=*")
    # options.add_argument("--disable-features=AsyncDns")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")

    
    try:
        async with webdriver.Chrome(options=options) as driver:
            # os.system('cls') # Windows
            os.system('clear')  # Linux/Mac
            await driver.delete_all_cookies()
            info = f"{datetime.now().strftime('%m/%d')} {datetime.now().strftime('%H:%M') if random_wait == 0 else (datetime.strptime('12:00', '%H:%M') + timedelta(seconds=random_wait)).strftime('%H:%M')} {random_Q}"
            print(info)
            # Notifier.notify(info, title="Anki Automation")
            notify(info)
            # notify("Anki Automation", info)
            if not test: 
                while datetime.now().strftime("%H:%M") <= "12:00": time.sleep(60) # Disable this line to test
            time.sleep(random_wait)
            await login(driver)
            await practice(driver, random_Q)
    except Exception as e:
        print(f"Error running AnkiWeb automation: {e}")
        # Notifier.notify(f"Error running AnkiWeb automation: {e}", title="Anki Automation")
        notify(f"Error running AnkiWeb automation: {e}")
        # notify("Anki Automation", f"Error running AnkiWeb automation: {e}")
        raise

    # await close_all_chrome()

test = True
# Notifier.notify("Program is starting", title="Anki Automation")
# notify("Anki Automation", "Program is starting")
asyncio.run(AnkiWeb(test))
# asyncio.run(close_all_chrome())
# Notifier.notify("Done", title="Anki Automation")
notify("Done")

# try:
#     # import subprocess
#     subprocess.run(['pkill', '-f', 'selenium_driverless'], capture_output=True)
#     subprocess.run(['rm', '-rf', '/tmp/chrome-profile'], shell=True, capture_output=True)
# except:
#     pass

# if pgrep "Google Chrome" > /dev/null; then
#     killall "Google Chrome"
# fi

# set pythonPath to "/Users/hsiao/.pyenv/versions/3.10.11/bin/python"
# set scriptPath to "/Users/hsiao/Github/VisualStudioCode/Python/Bots/Anki/Review/auto_web_intosh.py"
# do shell script "env -i PATH=$PATH HOME=$HOME " & pythonPath & " " & scriptPath