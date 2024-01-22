from selenium import webdriver
import chardet
import pyperclip
import time
import win32clipboard as wc
import win32con
import os
from PIL import Image, ImageGrab
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import win32gui, win32com.client
import pyautogui

abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
# driver = webdriver.Firefox()
# driver.get("https://www.google.com")

#words = open('Anki_web/pending.txt')
#for word in words.readlines():
#    print(word)
#words.close()

# text = open('Anki_web/KK.txt', 'rb').read()
# print(chardet.detect(text))
# print(text)
# print(text.decode('iso-8859-9').encode('utf8'))
# driver.close()

# previous = pyperclip.is_available()
# while True:
#     if previous != pyperclip.is_available():
#         break
#     time.sleep(0.1)
# print(1)
previous = ""

# while True:
#     wc.OpenClipboard()
#     # wc.EmptyClipboard()
#     # print("start")
#     try:
#         current = wc.GetClipboardData(win32con.CF_DIB)
#     except TypeError:
#         # Ignore unsupported data types
#         os.system("cls")
#         print("waiting for copying")
#         wc.CloseClipboard()
#         time.sleep(10)
#         continue
#     if current != previous:
#         wc.EmptyClipboard()
#         break
#     time.sleep(0.1)
#     wc.CloseClipboard()
# print(current)
    # time.sleep(5)
    # image = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    # if image is None:
    #     print("error")
    # else:
    #     print("yep")
    # wc.EmptyClipboard()
    # wc.CloseClipboard()

# pyperclip.waitForNewPaste()
#     # print("waiting")
#     # time.sleep(3)
# image = ImageGrab.grabclipboard()
# print("done")

# content = "abc 123 一二三"
# pyperclip.copy(content)

# words = open('Anki_web/pending.txt', 'r')
# index = words.readline().replace('\n','') #去掉換行

# while index:
# 	print(index)
# 	index = words.readline().replace('\n','') #去掉換行
# words.close()

# with open('Anki_web/pending.txt','r') as words:
#     temp = words.read()
#     list = temp.split('\n')
# for index in list:
#     print(index)

# index = "consecutive"
# service = Service(executable_path = "geckodriver")
# driver = webdriver.Firefox(service = service)
# driver.get("https://dictionary.cambridge.org/zht/")
# driver.implicitly_wait(5)
# search_bar = driver.find_element(By.ID, "searchword")
# search_button = driver.find_element(By.CLASS_NAME, "bo.iwc.iwc-40.hao.lb0.cdo-search-button.lp-0")
# search_bar.send_keys(index)
# search_button.submit()
# content = driver.find_element(By.CSS_SELECTOR, "div.def-block.ddef_block").text
# print(content)
# OfNoUse = True
# content = content[content.find("\n") + 1:]
# try: 
#     driver.find_element(By.CSS_SELECTOR, "span.epp-xref.dxref")
#     print(1)
# except: 
#     OfNoUse = False
#     print(2)
# if OfNoUse: content = content[content.find("\n") + 1:] #前兩行是無用資訊
# try: 
#     driver.find_element(By.CSS_SELECTOR, "span.def-info.ddef-info.gc.dgc")
#     print(3)
# except: 
#     OfNoUse = False
#     print(4)
# if OfNoUse: content = content[content.find("\n") + 1:] #前兩行是無用資訊
# print(content)
# driver.close()

# print(win32gui.FindWindow(None, "User 1 - Anki"))

# driver.set_window_position(0, 0)
# driver.set_window_size(1284, 1044)

# f = open('pending.txt', 'r')
# print(f)

pyautogui.hotkey('alt', 'tab')
Add_main_location = pyautogui.locateOnScreen(abs + '/screenshots/Add_main.png', confidence=0.9)
if Add_main_location is not None: print("found")