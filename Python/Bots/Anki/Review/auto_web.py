import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from applescript import AppleScript # pip install py-applescript

import time
import random
import asyncio

email_prefix = "hsiaoseanhs"
bir = 911119
remain = -1

async def close_all_chrome():
    AppleScript('''
                    if application "Google Chrome" is running then
                        tell application "Google Chrome" to quit
                    end if
                ''').run()

async def login(driver):
    await driver.get("https://ankiweb.net/account/login", wait_load=True)
    while True:
        try: Login = await driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg", timeout=1); break
        except: await driver.sleep(1)

    svelte = await driver.find_elements(By.CLASS_NAME, "form-control svelte-1ak1s42")
    await svelte[0].send_keys(email_prefix + "@gmail.com")
    await svelte[1].send_keys("sean" + str(bir))
    await Login.click()

async def practice(driver):
    while True:
        try:
            element = await driver.find_element(By.XPATH, "//*[text()='(02)English']", timeout=1)
            await element.click()
            break
        # except Exception as e: print("Study page:", e); await driver.sleep(1)
        except: await driver.sleep(1)
    
    while True:
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
                            print(f" Good 10m({remain})")
                        elif goodtime == "01d":
                            await btn[2].click()
                            print(f" Good 01d({remain})")
                        else:
                            R = random.random()
                            if R <= 0.3:
                                await btn[2].click()
                                print(f" Good ran({remain})")
                            elif R <= 0.6:
                                await btn[1].click()
                                print(f" Hard ran({remain})")
                            else:
                                await btn[0].click()
                                print(f"Again ran({remain})")
                        break
                # except Exception as e: print("btn:", e); await driver.sleep(1)
                except: await driver.sleep(1)
        # except Exception as e: print("Ans loop:", e); await driver.sleep(1)
        except: await driver.sleep(1)

async def AnkiWeb():
    await close_all_chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    options.add_argument("--headless")
    async with webdriver.Chrome(options=options) as driver:
        await login(driver)
        await practice(driver)
        await driver.sleep(999)

asyncio.run(AnkiWeb())