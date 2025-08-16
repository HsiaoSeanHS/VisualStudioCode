import os
import time
import random
import asyncio
import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

from datetime import datetime, timedelta
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

email_prefix = "hsiaoseanhs"
bir = 911119
remain = -1

async def close_all_chrome():
    try: os.system('taskkill /F /IM "chrome.exe"') # Windows
    except: pass

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

async def AnkiWeb():
    await close_all_chrome()
    os.system('cls') # Windows
    random_wait, random_Q = random.randint(12, 34567), random.randint(20, 60)
    # random_wait, random_Q = 0, 5
    if random_wait <= (datetime.now() - datetime.combine(datetime.now().date(), datetime.strptime("12:00", "%H:%M").time())).total_seconds(): random_wait = 0
    print(
        datetime.now().strftime("%m/%d"),
        datetime.now().strftime("%H:%M") if random_wait == 0 else (datetime.strptime("12:00", "%H:%M") + timedelta(seconds=random_wait)).strftime("%H:%M"),
        random_Q
    )
    while datetime.now().strftime("%H:%M") <= "12:00": time.sleep(60)
    time.sleep(random_wait)
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    options.add_argument("--headless")
    async with webdriver.Chrome(options=options) as driver:
        await login(driver)
        await practice(driver, random_Q)

asyncio.run(AnkiWeb())

# Use for build executable file
# pyinstaller -F --collect-all "selenium_driverless" ./AnkiWeb_win.py