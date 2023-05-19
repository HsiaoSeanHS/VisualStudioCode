
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


service = Service(executable_path = "geckodriver")
driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://dictionary.cambridge.org/zht/")
driver.implicitly_wait(5)
word = "fine"

#search_bar = driver.find_element(By.ID, "APjFqb")
#search_button = driver.find_element(By.CLASS_NAME, "gNO89b")
#search_bar.send_keys(word)
#search_button.submit()
#result_class = driver.find_element(By.CLASS_NAME, "yuRUbf")
#result_address = result_class.find_element(By.PARTIAL_LINK_TEXT, "fine")[1]
#driver.execute_script("arguments[0].scrollIntoView();", result_address)
#result_address.submit()
search_bar = driver.find_element(By.ID, "searchword")
search_button = driver.find_element(By.CLASS_NAME, "bo.iwc.iwc-40.hao.lb0.cdo-search-button.lp-0")
search_bar.send_keys(word)
search_button.submit()

part_of_speech = driver.find_element(By.CSS_SELECTOR, "span.pos.dpos").text
# print(part_of_speech)
pronounce = driver.find_element(By.CSS_SELECTOR, "span.us.dpron-i span.ipa.dipa.lpr-2.lpl-1").text
# print(pronounce)
content = driver.find_element(By.CSS_SELECTOR, "div.def-block.ddef_block").text
# while '\n' not in content:
# content.splitlines()
# for i in content:
#     if i != "\n":
#         content = content.lstrip()
#     elif i == "\n":
#         content = content.lstrip()
#         break
# line = "\n"
# lines = (line.strip() for line in content)
# for line in lines:
#     print(line)
right_mid_bracket = content.find("]")
if right_mid_bracket != -1: content = content[right_mid_bracket+2:] #前兩行是無用資訊
# else: content = content
print(content)


