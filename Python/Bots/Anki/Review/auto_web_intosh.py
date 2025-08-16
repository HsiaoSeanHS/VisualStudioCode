import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import os
import time
import random
import asyncio
from datetime import datetime, timedelta

from selenium_driverless import webdriver
from selenium_driverless.types.by import By

from applescript import AppleScript

email_prefix = "hsiaoseanhs"
bir = 911119
remain = -1

# async def close_all_chrome():
#     try: os.system('taskkill /F /IM "chrome.exe"') # Windows
#     except: pass
async def close_all_chrome():
    try:
        # Kill all selenium-driverless Chrome processes
        os.system('pkill -f "selenium_driverless" 2>/dev/null')
        os.system('pkill -f "Google Chrome.*remote-debugging-port" 2>/dev/null')
        
        # Also try AppleScript for any regular Chrome instances
        AppleScript('''
                        if application "Google Chrome" is running then
                            tell application "Google Chrome" to quit
                        end if
                    ''').run()
        
        # Wait a moment for processes to terminate
        await asyncio.sleep(2)
        
        # Clean up selenium-driverless cache directory
        selenium_cache_dir = os.path.expanduser('~/Library/Application Support/selenium-driverless')
        if os.path.exists(selenium_cache_dir):
            try:
                import shutil
                shutil.rmtree(selenium_cache_dir)
                # print("Cleaned selenium-driverless cache directory")
            except Exception as e:
                print(f"Warning: Could not clean cache directory: {e}")
        
        # Recreate the directory to avoid FileNotFoundError
        try:
            os.makedirs(selenium_cache_dir, exist_ok=True)
        except Exception as e:
            print(f"Warning: Could not recreate cache directory: {e}")
        
        # Clean up any leftover selenium temp directories
        os.system('rm -rf /tmp/selenium_driverless_* 2>/dev/null')
        os.system('rm -rf /var/folders/*/T/selenium_driverless_* 2>/dev/null')
        
        # Force garbage collection to free up resources
        import gc
        gc.collect()
        
    except Exception as e:
        print(f"Warning: Error closing Chrome processes: {e}")
        pass

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
                        elif goodtime == "01d":
                            await btn[2].click()
                            print(f"G 01d({remain}){count}")
                        else:
                            R = random.random()
                            if R <= 0.3:
                                await btn[2].click()
                                print(f"G ran({remain}){count}")
                            elif R <= 0.6:
                                await btn[1].click()
                                print(f"H ran({remain}){count}")
                            else:
                                await btn[0].click()
                                print(f"A ran({remain}){count}")
                        count -= 1
                        break
                # except Exception as e: print("btn:", e); await driver.sleep(1)
                except: await driver.sleep(1)
        # except Exception as e: print("Ans loop:", e); await driver.sleep(1)
        except: await driver.sleep(1)

async def AnkiWeb(test):
    # Increase file descriptor limit to prevent "too many open files" error
    try:
        import resource
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        print(f"Current file descriptor limits: soft={soft}, hard={hard}")
        # Try to increase the soft limit to the hard limit
        resource.setrlimit(resource.RLIMIT_NOFILE, (min(hard, 8192), hard))
        new_soft, _ = resource.getrlimit(resource.RLIMIT_NOFILE)
        print(f"New soft limit: {new_soft}")
    except Exception as e:
        print(f"Warning: Could not increase file descriptor limit: {e}")
    
    await close_all_chrome()
    if test:
        random_wait, random_Q = 0, 5
    else:
        random_wait, random_Q = random.randint(12, 34567), random.randint(20, 60)
    if random_wait <= (datetime.now() - datetime.combine(datetime.now().date(), datetime.strptime("12:00", "%H:%M").time())).total_seconds(): random_wait = 0
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--max_old_space_size=4096")
    options.add_argument("--disable-features=TranslateUI")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-dns-prefetch")
    options.add_argument("--disable-dns-over-https")
    options.add_argument("--dns-prefetch-disable")
    
    try:
        async with webdriver.Chrome(options=options) as driver:
            # os.system('cls') # Windows
            os.system('clear')  # Linux/Mac
            print(
                datetime.now().strftime("%m/%d"),
                datetime.now().strftime("%H:%M") if random_wait == 0 else (datetime.strptime("12:00", "%H:%M") + timedelta(seconds=random_wait)).strftime("%H:%M"),
                random_Q
            )
            if not test: 
                while datetime.now().strftime("%H:%M") <= "12:00": time.sleep(60) # Disable this line to test
            time.sleep(random_wait)
            await login(driver)
            await practice(driver, random_Q)
    except Exception as e:
        print(f"Error running AnkiWeb automation: {e}")
        raise

    await close_all_chrome()

test = False
asyncio.run(AnkiWeb(test))

try:
    import subprocess
    subprocess.run(['pkill', '-f', 'selenium_driverless'], capture_output=True)
    subprocess.run(['rm', '-rf', '/tmp/selenium_driverless_*'], shell=True, capture_output=True)
except:
    pass