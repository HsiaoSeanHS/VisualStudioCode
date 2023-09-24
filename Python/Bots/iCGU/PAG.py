import os, time
import pyautogui

abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"
time.sleep(5)
os.system('cls')
while True:
    times = 0
    search_location = pyautogui.locateOnScreen(abs + "search.jpg", confidence=0.9)
    if search_location is not None:
        search_center = pyautogui.center(search_location)
    else: 
        print("wrong page")
        exit()
    while times < 60:
        if pyautogui.locateOnScreen(abs + "NoClass.jpg", confidence=0.9) is not None: 
            print('No Class')
            print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
            time.sleep(60)
            continue
        pyautogui.click(search_center.x, search_center.y)
        add_location = pyautogui.locateOnScreen(abs + "add.jpg", confidence=0.9)
        if add_location is not None:
            NoChen_location = pyautogui.locateOnScreen(abs + "NoChen.jpg", confidence=0.9)
            if NoChen_location is None:
                add_center = pyautogui.center(add_location)
                pyautogui.click(add_center.x, add_center.y)
                time.sleep(0.1)
                sure_location = pyautogui.locateOnScreen(abs + "sure.jpg", confidence=0.9)
                while sure_location is None: sure_location = pyautogui.locateOnScreen(abs + "sure.jpg", confidence=0.9)
                # pyautogui.press('enter')
                print("success")
                print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
                break
            else: print('shit')
        times += 1
        time.sleep(0.4)
