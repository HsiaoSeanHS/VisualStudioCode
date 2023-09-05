import os, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def rand(last): return random.randint(0, last)
def randAgent():
    Mozilla = "Mozilla/5.0 "
    System = ["(Windows NT 10.0; Win64; x64) ",
            "(X11; Linux x86_64) ",
            "(Macintosh; Intel Mac OS X 10_15_7) ",
            "(Macintosh; Intel Mac OS X 13_1) "]
    AppleWebKit = ["AppleWebKit/537.36 (KHTML, like Gecko) ",
                "AppleWebKit/605.1.15 (KHTML, like Gecko) ",
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 "]
    Chrome = ["Chrome/108.0.0.0 ",
            "Chrome/109.0.0.0 "]
    Safari = ["Safari/537.36",
            "Safari/605.1.15"]
    Ar = rand(2)
    return Mozilla + System[rand(3)] + AppleWebKit[Ar] + (Chrome[rand(1)] if Ar != 2 else "") + Safari[rand(1)]

Agent = randAgent()
options = Options()
# options.headless = True
options.add_argument("--start-maximized")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("extensions.legacy.enabled", False)
options.set_preference("general.useragent.override", Agent)
driver = webdriver.Firefox(options = options)

os.system('cls')
driver.get('https://catalog.cgu.edu.tw/stucourse')

ID = input('ID: ')
driver.find_element(By.CLASS_NAME, 'form-control.ltr_override.input.ext-input.text-box.ext-text-box').send_keys(ID + "@cgu.edu.tw")
driver.find_element(By.CLASS_NAME, 'form-control.ltr_override.input.ext-input.text-box.ext-text-box').send_keys(Keys.ENTER)
PW = input('PW: ')
driver.find_element(By.CLASS_NAME, 'form-control.input.ext-input.text-box.ext-text-box').send_keys(PW)
driver.find_element(By.CLASS_NAME, 'form-control.input.ext-input.text-box.ext-text-box').send_keys(Keys.ENTER)
# driver.implicitly_wait(5)
time.sleep(2)
# print(driver.find_element(By.CLASS_NAME, 'display-sign-container').text)
print('請在手機輸入: ' + driver.find_element(By.CLASS_NAME, 'display-sign-container').text)
while True:
    try: 
        driver.find_element(By.CLASS_NAME, 'win-button.button_primary.button.ext-button.primary.ext-primary').click()
        break
    except: 
        time.sleep(1)
        continue
