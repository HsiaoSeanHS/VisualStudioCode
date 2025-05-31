import os, time
import pyautogui

pyautogui.PAUSE = 0.5
MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
abs = MainPath + "/screenshots/VPN/"
VPN_count = 0

def Open_OpenVPN():
    pyautogui.hotkey('shift', 'command', 'H')
    time.sleep(1)
    OpenVPN_location = pyautogui.locateOnScreen(abs + 'OpenVPN.png', confidence=0.9)
    # print(pyautogui.locateOnScreen(abs + 'OpenVPN.png', confidence=0.9))
    if OpenVPN_location is not None:
        OpenVPN_center = pyautogui.center(OpenVPN_location)
        pyautogui.click(OpenVPN_center.x/2, OpenVPN_center.y/2) 
        pyautogui.click(OpenVPN_center.x/2, OpenVPN_center.y/2)
        # print("click!")
    else: print("OpenVPN fail")
    time.sleep(3)

def Open_VPNGate():
    pyautogui.hotkey('shift', 'command', 'H')
    time.sleep(1)
    VPNGate_location = pyautogui.locateOnScreen(abs + 'VPNGate.png', confidence=0.9)
    while VPNGate_location is not None:
    # if VPNGate_location is not None:
        VPNGate_center = pyautogui.center(VPNGate_location)
        pyautogui.click(VPNGate_center.x/2, VPNGate_center.y/2)
        pyautogui.click(VPNGate_center.x/2, VPNGate_center.y/2)
    # else: print("VPNGate fail")
        time.sleep(10)
        try: VPNGate_location = pyautogui.locateOnScreen(abs + 'VPNGate.png', confidence=0.9)
        except: 
            # print("VPNGate start")
            break

def Connect(new_VPN):
    if new_VPN:
        # print("if")
        # time.sleep(1)
        # pyautogui.press('down')
        # pyautogui.press('enter')
        Disconnected_location = pyautogui.locateOnScreen(abs + 'Disconnected.png', confidence=0.9)
        Disconnected_center = pyautogui.center(Disconnected_location)
        pyautogui.click(Disconnected_center.x/2, Disconnected_center.y/2)
        time.sleep(10)
        try:
            Connect_failed_location = pyautogui.locateOnScreen(abs + 'Connect_failed.png', confidence=0.9)
            if Connect_failed_location is not None:
                # VPN connect fail
                # pyautogui.click(Disconnected_center.x, Disconnected_center.y)
                pyautogui.press('right')
                pyautogui.press('right')
                pyautogui.press('enter')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.press('enter')
                # Delete VPN
                Add_VPN(VPN_count)
                Connect(True)
        except: print("VPN connected")
    else: # Old VPN
        # print("else")
        Open_OpenVPN()
        # print("openvpn")
        try:
            Disconnected_location = pyautogui.locateOnScreen(abs + 'Disconnected.png', confidence=0.9)
            while Disconnected_location is not None:
                pyautogui.press('down')
                # for Disconnected_location in Disconnected_locationS:
                    # Disconnected_center = pyautogui.center(Disconnected_location)
                    # pyautogui.click(Disconnected_center.x, Disconnected_center.y)
                    
                pyautogui.press('enter')
                time.sleep(10)
                try:
                    Connect_failed_location = pyautogui.locateOnScreen(abs + 'Connect_failed.png', confidence=0.9)
                    if Connect_failed_location is not None:
                        # VPN connect fail
                        # pyautogui.click(Disconnected_center.x, Disconnected_center.y)
                        pyautogui.press('enter') # Turn off
                        pyautogui.press('right')
                        pyautogui.press('enter')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        time.sleep(1)
                        continue
                except: 
                    print("VPN connected")
                    break
        except:
            # No VPN in list
            # pyautogui.hotkey('shift', 'command', 'H')
            # time.sleep(1)
            Add_VPN(VPN_count)
            Connect(True)

def Add_VPN(VPN_count):
    distance = 10; elements = []
    Open_VPNGate()
    if VPN_count != 0:
        for i in range(VPN_count): # VPN used last time
            pyautogui.press('down')
    else: pyautogui.press('down'); VPN_count += 1
    # OfNoUse_location = pyautogui.locateOnScreen(abs + '219.png', confidence=0.9)
    # while OfNoUse_location is not None:
    #     pyautogui.press('down'); VPN_count += 1
    OfNoUse_locations = pyautogui.locateAllOnScreen(abs + '219.png', confidence=0.9)
    while True:
        for element in OfNoUse_locations:
            if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
                elements.append(element)
        # print(len(elements))
        if len(elements) <= 6: 
            elements = []
            break
        elements = []
        pyautogui.press('down'); VPN_count += 1
        OfNoUse_locations = pyautogui.locateAllOnScreen(abs + '219.png', confidence=0.9)
    try:
        Detail_location = pyautogui.locateOnScreen(abs + 'Detail.png', confidence=0.9)
        if Detail_location is not None:
            Ad_location = pyautogui.locateOnScreen(abs + 'Ad.png', confidence=0.9)
            while Ad_location is None:
                time.sleep(1)
                Ad_location = pyautogui.locateOnScreen(abs + 'Ad.png', confidence=0.9)
            Ad_center = pyautogui.center(Ad_location)
            pyautogui.click(Ad_center.x/2, Ad_center.y/2)
    except: pass # No Ad

    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    # OpenVPN
    pyautogui.press('enter')
    pyautogui.press('enter')


# Connect(False)
# pyautogui.hotkey('command', 'Tab')
# pyautogui.click(1000,1000)
# Add_VPN(0)
# Connect(False)