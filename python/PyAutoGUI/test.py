import os
import PIL
#import subprocess
import pyautogui
import random
import keyboard
import win32gui, win32api
from time import sleep, time
import time
import win32com.client

pyautogui.PAUSE = 0.5 
print(random.randint(0,1))
# if(win32gui.FindWindow(None, "User 1 - Anki") == 0):
#     os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
#     time.sleep(10)
#     shell = win32com.client.Dispatch("WScript.Shell")
#     shell.AppActivate("User 1 - Anki")
# else: 
#     os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
# time.sleep(3)
# print(pyautogui.locateOnScreen('screenshots/10min.png', confidence=0.9))
# win32api.ShellExecute(0, 'open', 'C:\\Program Files\\Anki\\anki.exe', '','',1)
# os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
# time.sleep(5)
# shell = win32com.client.Dispatch("WScript.Shell")
# shell.AppActivate("User 1 - Anki")
# Anki = win32gui.FindWindow(None, "User 1 - Anki")
# print(1)
# time.sleep(5)
# os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
# time.sleep(5)
# os.system('%s%s' % ("taskkill /F /IM ","Anki.exe"))
# shell = win32com.client.Dispatch("WScript.Shell")
# shell.AppActivate("User 1 - Anki")
# Anki = win32gui.FindWindow(None, "User 1 - Anki")
# print(Anki)
# pyautogui.hotkey('alt', 'tab')
# pyautogui.moveTo(1895, 15, duration = 0)
# aDay_location = pyautogui.locateOnScreen('screenshots/1d.png', confidence=0.9)
# print(aDay_location)