import os, time, pyautogui

pyautogui.PAUSE = 0.5
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"

while(True):
    try:
        showlesson_location = pyautogui.locateOnScreen(abs + 'show_lesson.png', confidence=0.9)
        if showlesson_location is not None:
            showlesson_center = pyautogui.center(showlesson_location)
            pyautogui.moveTo(showlesson_center.x, showlesson_center.y)
    except: time.sleep(1); continue
    try:
        cantlistennow_location = pyautogui.locateOnScreen(abs + "can't_listen_now_gray.png", confidence=0.9)
        if cantlistennow_location is not None:
            pyautogui.click()
            cantlistennow_center = pyautogui.center(cantlistennow_location)
            pyautogui.click(cantlistennow_center.x, cantlistennow_center.y); time.sleep(1)
            pyautogui.moveTo(showlesson_center.x, showlesson_center.y); time.sleep(870)
    except: time.sleep(1)