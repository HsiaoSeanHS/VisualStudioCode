import os, time, pyautogui

def findANDclick(button_name, sleep):
    button_location = pyautogui.locateOnScreen(abs + button_name + '.png', confidence=0.9)
    if button_location is not None:
        button_center = pyautogui.center(button_location)
        pyautogui.click(button_center.x, button_center.y)
        time.sleep(sleep)
        return True
    else: time.sleep(0.5); return False

times = 0
pyautogui.PAUSE = 0.5
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"

os.system("start C:\\Users\\Public\\Desktop\\Duo.lnk"); time.sleep(5)
findANDclick('start', 5); findANDclick('back', 1); pyautogui.scroll(300); findANDclick('rookie_review', 1)

while(True):
    findANDclick('check', 0.5)
    doing = findANDclick('practice', 0.5)
    times += 1 if doing is False else 0
    if times > 25:
        findANDclick('back', 1)
        pyautogui.scroll(300)
        findANDclick('rookie_review', 1)
        times = 0
