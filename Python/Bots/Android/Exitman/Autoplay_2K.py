import os, time, pyautogui
import win32gui, win32com.client

def move(direct, distance):
    second = abs(distance) * 0.00035
    # times = int(round(abs(distance)/50, 0))
    if direct == "left":
        # for i in range(times):
            # pyautogui.press('left')
            # i = i + 1
        pyautogui.keyDown('left')
        time.sleep(second)
        pyautogui.keyUp('left')
    elif direct == "right":
        # for i in range(times):
        #     pyautogui.press('right')
        #     i = i + 1
        pyautogui.keyDown('right')
        time.sleep(second)
        pyautogui.keyUp('right')

def dL():
    HeadLose_location = pyautogui.locateOnScreen(ABS + 'head_lose_2K.jpg', confidence=0.9)
    try: 
        HeadLose_center = pyautogui.center(HeadLose_location)
        print("Not yet")
        return False
    except:
        print("Lose")
        return True

os.system("cls")
try:
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("ExitMan")
    Exitman = win32gui.FindWindow(None, "ExitMan")
    print("opened")
except:
    os.system("cd C:\\Users\\hsiao\\AppData\\Local\\Microsoft\\WindowsApps\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe")
    os.system("WsaClient.exe /launch wsa://exitman.burukuri")
    print("will open")
    time.sleep(5)
# pyautogui.PAUSE = 0.1
ABS = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"
while True:
    try:
        Start_location = pyautogui.locateOnScreen(ABS + 'start_2K.jpg', confidence=0.9, grayscale=True)
        # print(Start_location)
        if Start_location is not None:
            Start_center = pyautogui.center(Start_location)
            pyautogui.click(Start_center.x, Start_center.y)
            print("Click on start")
            time.sleep(0.2)
            Pause_location = pyautogui.locateOnScreen(ABS + 'pause_2K.jpg', confidence=0.9, grayscale=True)
            if Pause_location is None: continue
            break
    except: 
        print("can't find start button")
        time.sleep(2)
        continue
# t = 0
# start = time.time()
# time.sleep(1)
Situation = ""
while True:
    # pyautogui.keyUp('right')
    # pyautogui.keyUp('left')
    Head_location = pyautogui.locateOnScreen(ABS + 'head_2K.jpg', confidence=0.9, grayscale=True)
    if Head_location is not None:
        print("found head")
        Head_center = pyautogui.center(Head_location)
        Start_location = pyautogui.locateOnScreen(ABS + 'start_2K.jpg', confidence=0.9, grayscale=True)
        # print(Start_location)
        if Start_location is not None:
            Start_center = pyautogui.center(Start_location)
            pyautogui.click(Start_center.x, Start_center.y)
            print("Click on start")
            time.sleep(0.2)
            # Pause_location = pyautogui.locateOnScreen(ABS + 'pause_2K.jpg', confidence=0.9, grayscale=True)
            # if Pause_location is None: continue
            # break
    else:
        if Situation != "Head": 
            print("can't find head")
            Situation = "Head"
        # else: break
        continue
        # break
    Exit_location = pyautogui.locateOnScreen(ABS + 'Exit_2K.jpg', confidence=0.9)
    if Exit_location is not None:
        Exit_center = pyautogui.center(Exit_location)
        distanceE = Exit_center.x - Head_center.x
        # distanceC = 1440 - Exit_center.x
        if abs(distanceE) < 100: time.sleep(2); continue
        if distanceE > 0: #turn right
            print("Turn right")
            move("right", distanceE)
        elif distanceE < 0: #turn left
            print("Turn left")
            move("left", distanceE)
        else: 
            # time.sleep(1)
            continue # No need to move
    else:
        if Situation != "Exit": 
            print("can't detect Exit")
            Situation = "Exit"
        # else: break
        continue
        # if t > 0: break
        # t += 1
        # time.sleep(2)
        Restart_location = pyautogui.locateOnScreen(ABS + 'restart_2K.jpg', confidence=0.9, grayscale=True)
        RestartVid_location = pyautogui.locateOnScreen(ABS + 'restart_vid_2K.jpg', confidence=0.9, grayscale=True)
        if Restart_location is not None:
            Restart_center = pyautogui.center(Restart_location)
            pyautogui.click(Restart_center.x, Restart_center.y)
        elif RestartVid_location is not None:
            RestartVid_center = pyautogui.center(RestartVid_location)
            pyautogui.click(RestartVid_center.x, RestartVid_center.y)
        else:
            print("can't detect Exit")
            continue
print("End Game.")  
            