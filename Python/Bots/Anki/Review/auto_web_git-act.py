import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import os
import time
import random
import asyncio
from datetime import datetime, timedelta

from selenium_driverless import webdriver
from selenium_driverless.types.by import By

email_prefix = "hsiaoseanhs"
bir = 911119
remain = -1

class Selenium:
    def __init__(self):
        self.driver = None

    async def login(self):
        while True:
            try: 
                await self.driver.get("https://ankiweb.net/account/login", wait_load=True)
                Login = await self.driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg", timeout=1)
                svelte = await self.driver.find_elements(By.CLASS_NAME, "form-control svelte-1ak1s42")
                await svelte[0].send_keys(email_prefix + "@gmail.com")
                await svelte[1].send_keys("sean" + str(bir))
                await Login.click()
                break
            except: 
                await self.driver.sleep(1)

    async def practice(self, target):
        while True:
            try:
                element = await self.driver.find_element(By.XPATH, "//*[text()='(02)English']", timeout=1)
                await element.click()
                break
            except: await self.driver.sleep(1)

        count = target
        while count > 0:
            try:
                element = await self.driver.find_element(By.XPATH, "//*[text()='Show Answer']", timeout=1)
                await element.click()
                await self.driver.sleep(random.randint(50,60))
                while True:
                    try:
                        btn = await self.driver.find_elements(By.CLASS_NAME, "btn btn-primary btn-lg m-1", timeout=1)
                        if len(btn) == 4: 
                            remain = await self.driver.find_element(By.CSS_SELECTOR, 'div.float-end')
                            remain = await remain.text
                            remain = remain.replace("\n", "")
                            goodtime = await self.driver.find_element(By.XPATH, '//*[@id="ansarea"]/div/div[3]/div')
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
                    except: await self.driver.sleep(1)
            except: await self.driver.sleep(1)

    async def async__init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument("--mute-audio")
        options.add_argument("--headless=new")
        options.add_argument("--no-proxy-server")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-features=NetworkService")
        self.driver = await webdriver.Chrome(options=options)
        try:
            await self.driver.delete_all_cookies()
            await self.login()
            await self.practice(random_Q)
            await self.driver.quit()
        except Exception as e:
            print(f"Error running AnkiWeb automation: {e}")

test = False
if test:
    random_wait, random_Q = 0, 5
else:
    random_wait, random_Q = random.randint(12, 34567), random.randint(20, 60)
    # if random_wait <= (datetime.now() - datetime.combine(datetime.now().date(), datetime.strptime("12:00", "%H:%M").time())).total_seconds(): random_wait = 0
info = f"{datetime.now().strftime('%m/%d')} {datetime.now().strftime('%H:%M')}  {random_Q}" # if random_wait == 0 else (datetime.strptime('12:00', '%H:%M') + timedelta(seconds=random_wait)).strftime('%H:%M')} {random_Q}"
print(info)
    # if not test: 
    #     while datetime.now().strftime("%H:%M") <= "12:00": time.sleep(60) # Disable this line to test
    # time.sleep(random_wait)
sln = Selenium()
asyncio.run(sln.async__init__())
