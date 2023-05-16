import os
import PIL
import keyboard
import time
import random
import win32gui, win32api, win32com.client
import pyautogui

def CheckAnki():
    if(win32gui.FindWindow(None, "User 1 - Anki") == 0):
        os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
        time.sleep(10)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("User 1 - Anki")
    else: os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
    time.sleep(3)

x = 0
pyautogui.PAUSE = 0.5
os.system('%s%s' % ("taskkill /F /IM ","Anki.exe"))
os.system("cls")
os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
time.sleep(10)
shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("User 1 - Anki")
Anki = win32gui.FindWindow(None, "User 1 - Anki")
if Anki != 0:
    English_location = pyautogui.locateOnScreen('screenshots/English.png', confidence=0.9)
    if English_location is not None:
        English_center = pyautogui.center(English_location)
        pyautogui.click(English_center.x, English_center.y)
    StudyNow_location = pyautogui.locateOnScreen('screenshots/StudyNow.png', confidence=0.9)
    if StudyNow_location is not None:
        StudyNow_center = pyautogui.center(StudyNow_location)
        pyautogui.click(StudyNow_center.x, StudyNow_center.y)
    ShowAnswer_location = pyautogui.locateOnScreen('screenshots/ShowAnswer.png', confidence=1)
    pyautogui.press('space')
    time.sleep(60)
    CheckAnki()
    Good_location = pyautogui.locateOnScreen('screenshots/Good.png', confidence=0.9)
    if Good_location is not None:
        Good_center = pyautogui.center(Good_location)
        while Good_location or Easy_location is not None:
            x += 1
            Easy_location = pyautogui.locateOnScreen('screenshots/Easy.png', confidence=0.9)
            Easy_center = pyautogui.center(Easy_location)
            Lower10min_location = pyautogui.locateOnScreen('screenshots/10min.png', confidence=0.9)
            aDay_location = pyautogui.locateOnScreen('screenshots/1d.png', confidence=0.9)
            if Lower10min_location is not None:
                Lower10min_center = pyautogui.center(Lower10min_location)
                if Lower10min_center.x >= 1600: 
                    pyautogui.click(Good_center.x, Good_center.y)
                    print(x, "Good 10m")
                elif aDay_location is not None:
                    aDay_center = pyautogui.center(aDay_location)
                    if aDay_center.x >= 1600: 
                        pyautogui.click(Good_center.x, Good_center.y)
                        print(x, "Good 1d")
                    else: 
                        pyautogui.click(Easy_center.x, Easy_center.y)
                        print(x, "Easy Left1d")
                else: 
                    if random.random() >= 0.7:
                        pyautogui.click(Easy_center.x, Easy_center.y)
                        print(x, "Easy Left10min&no1d")
                    else:
                        pyautogui.click(Good_center.x, Good_center.y)
                        print(x, "Good rand")
            else: 
                pyautogui.click(Easy_center.x, Easy_center.y)
                print(x, "Easy no10min")
            pyautogui.press('space')
            time.sleep(random.randint(50,60))
            CheckAnki()
            Good_location = pyautogui.locateOnScreen('screenshots/Good.png', confidence=0.9)
            if Good_location is None:
                Sync_location = pyautogui.locateOnScreen('screenshots/Sync.png', confidence=0.9)
                Sync_center = pyautogui.center(Sync_location)
                pyautogui.click(Sync_center.x, Sync_center.y)
                break
        print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
        os.system('%s%s' % ("taskkill /F /IM ","Anki.exe"))
    else: print("Wrong window or page")
else: print("Anki open fail")