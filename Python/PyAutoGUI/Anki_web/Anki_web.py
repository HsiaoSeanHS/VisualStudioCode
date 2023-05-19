
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(executable_path = "geckodriver")
driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://dictionary.cambridge.org/zht/")
driver.implicitly_wait(5)
index = "fine"

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
search_bar.send_keys(index)
search_button.submit()

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
# right_mid_bracket = content.find("]")
# dontknow = content[right_mid_bracket+1]
# if dontknow == '\n': print("_")
# print(dontknow, type(dontknow))
# if right_mid_bracket != -1: content = content[right_mid_bracket+2:] 
content = content[content.find("\n", content.find("\n")+1) + 1:] #前兩行是無用資訊
count = 0; start = 0 #content.find('\n') + 1  # Find the position of the second '\n'
while count >= 0:
    n = content.find("\n",start)
    if n == -1: break
    else: count += 1
    if count % 2 == 1: content = content[:n] + " " + content[n+1:]
    elif count > 0: content = content[:n+1] + "-" + content[n+1:]
    start = n + 1
part_of_speech = driver.find_element(By.CSS_SELECTOR, "span.pos.dpos").text.title()
# part_of_speech = part_of_speech.title()
# print(part_of_speech)
content = part_of_speech + ".\n" + content
# print(content)

phoneme = driver.find_element(By.CSS_SELECTOR, "span.us.dpron-i span.ipa.dipa.lpr-2.lpl-1").text
# print(phoneme)

#image

Source = driver.current_url
# print(Source)

#Cloze
