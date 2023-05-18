
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com")
# time.sleep(3)
driver.implicitly_wait(5)
word = "fine"
# element = driver.find_element(By.CSS_SELECTOR, "input.gLFyf.gsfi")
# element.clear()
# element.send_keys(word)
# element.send_keys(Keys.RETURN)
search_bar = driver.find_element(By.ID, "APjFqb")
search_button = driver.find_element(By.CLASS_NAME, "gNO89b")
search_bar.send_keys(word)
search_button.submit()
