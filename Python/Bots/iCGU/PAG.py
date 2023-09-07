import os, time
import pyautogui

abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"
time.sleep(5)
os.system('cls')
while True:
    pyautogui.press('enter')
    add_location = pyautogui.locateOnScreen(abs + "add.jpg", confidence=0.9)
    if add_location is not None:
        NoChen_location = pyautogui.locateOnScreen(abs + "NoChen.jpg", confidence=0.9)
        if NoChen_location is None:
            add_center = pyautogui.center(add_location)
            pyautogui.click(add_center.x, add_center.y)
            time.sleep(0.1)
            sure_location = pyautogui.locateOnScreen(abs + "sure.jpg", confidence=0.9)
            while sure_location is None: sure_location = pyautogui.locateOnScreen(abs + "sure.jpg", confidence=0.9)
            print("success")
            print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
        else: print('shit')
    time.sleep(0.3)
