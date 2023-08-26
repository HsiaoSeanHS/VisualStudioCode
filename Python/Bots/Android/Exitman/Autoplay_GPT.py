import os
import time
import pyautogui

def turn_and_return(direction, screenshots_path, Head_center):
    if direction == 'right':
        turn_point = (1910, 1000)
        return_point = (10, 1000)
    elif direction == 'left':
        turn_point = (10, 1000)
        return_point = (1910, 1000)
    else:
        return

    while Exit_center.x != Head_center.x:
        pyautogui.mouseDown(button='left')
        Exit_location = pyautogui.locateOnScreen(screenshots_path + 'Exit.jpg', confidence=0.9)
        if Exit_location is None:
            pyautogui.mouseUp(button='left')
            print(f'{direction} turn fail')
            break
        Head_location = pyautogui.locateOnScreen(screenshots_path + 'head.jpg', confidence=0.9)
        Head_center = pyautogui.center(Head_location)
        pyautogui.moveTo(return_point, duration=0)

    pyautogui.mouseUp(button='left')

# Clear the console screen
os.system("cls")

# Change directory
os.chdir(r"C:\Users\Hsiao Sean HS\AppData\Local\Microsoft\WindowsApps\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe")

# Launch the application
os.system("WsaClient.exe /launch wsa://exitman.burukuri")

time.sleep(5)

# Locate the Start button
screenshots_path = r'D:\CodeServer\Exitman_Autoplay\screenshots\\'
Start_location = pyautogui.locateOnScreen(screenshots_path + 'start.jpg', confidence=0.9)

if Start_location is not None:
    Start_center = pyautogui.center(Start_location)
    pyautogui.click(Start_center.x, Start_center.y)
    time.sleep(1)
else:
    print("Can't start the game")
    exit()

t = 0

while True:
    Head_location = pyautogui.locateOnScreen(screenshots_path + 'head.jpg', confidence=0.9)

    if Head_location is not None:
        Head_center = pyautogui.center(Head_location)
    else:
        print("Can't find head")
        break

    Exit_location = pyautogui.locateOnScreen(screenshots_path + 'Exit.jpg', confidence=0.9)

    if Exit_location is not None:
        Exit_center = pyautogui.center(Exit_location)

        if Exit_center.x > Head_center.x:
            turn_and_return('right', screenshots_path, Head_center)
            continue
        elif Exit_center.x < Head_center.x:
            turn_and_return('left', screenshots_path, Head_center)
            continue

        while Exit_location is None:
            time.sleep(0.5)
    else:
        if t > 0:
            break

        t += 1
        Restart_location = pyautogui.locateOnScreen(screenshots_path + 'restart.jpg', confidence=0.9)
        RestartVid_location = pyautogui.locateOnScreen(screenshots_path + 'restart_vid.jpg', confidence=0.9)

        if Restart_location is not None:
            Restart_center = pyautogui.center(Restart_location)
            pyautogui.click(Restart_center.x, Restart_center.y)
        elif RestartVid_location is not None:
            RestartVid_center = pyautogui.center(RestartVid_location)
            pyautogui.click(RestartVid_center.x, RestartVid_center.y)
        else:
            print("Can't detect Exit")
            break
