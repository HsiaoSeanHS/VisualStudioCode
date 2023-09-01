import os, time, pyautogui

def move(direct, distance):
    second = abs(distance) * 0.0007
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
    HeadLose_location = pyautogui.locateOnScreen(ABS + 'head_lose.jpg', confidence=0.9, region=(960,0,1080,960))
    try: 
        HeadLose_center = pyautogui.center(HeadLose_location)
        print("Not yet")
        return False
    except:
        print("Lose")
        return True

os.system("cls")
os.system("cd C:\\Users\\Hsiao Sean HS\\AppData\\Local\\Microsoft\\WindowsApps\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe")
os.system("WsaClient.exe /launch wsa://exitman.burukuri")
# time.sleep(15)
pyautogui.PAUSE = 0.1
ABS = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"
while True:
    try:
        Start_location = pyautogui.locateOnScreen(ABS + 'start.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,960))
        if Start_location is not None:
            Start_center = pyautogui.center(Start_location)
            pyautogui.click(Start_center.x, Start_center.y)
            Head_location = pyautogui.locateOnScreen(ABS + 'head.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,960))
            if Head_location is None: continue
            break
    except: 
        time.sleep(2)
        continue
# t = 0
# start = time.time()
# time.sleep(1)
Situation = ""
while True:
    pyautogui.keyUp('right')
    pyautogui.keyUp('left')
    Head_location = pyautogui.locateOnScreen(ABS + 'head.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,960))
    if Head_location is not None:
        Head_center = pyautogui.center(Head_location)
    else:
        if Situation != "Head": 
            print("can't find head")
            Situation = "Head"
        continue
        # break
    Exit_location = pyautogui.locateOnScreen(ABS + 'Exit.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,480))
    if Exit_location is not None:
        Exit_center = pyautogui.center(Exit_location)
        distanceE = Exit_center.x - Head_center.x
        # distanceC = 1440 - Exit_center.x
        if abs(distanceE) < 30: time.sleep(2); continue
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
        continue
        # if t > 0: break
        # t += 1
        # time.sleep(2)
        Restart_location = pyautogui.locateOnScreen(ABS + 'restart.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,960))
        RestartVid_location = pyautogui.locateOnScreen(ABS + 'restart_vid.jpg', confidence=0.9, grayscale=True, region=(960,0,1080,960))
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
            