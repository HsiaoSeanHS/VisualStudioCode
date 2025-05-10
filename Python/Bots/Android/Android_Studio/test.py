import os, subprocess, pyautogui
from subprocess import Popen, PIPE
from VPN import Open_OpenVPN, Open_VPNGate, Connect, Add_VPN

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
abs = MainPath + "/screenshots/VPN/"
# def activate_window(app_name):
#   """Activates a specific window based on application name and title."""
#   script = 'tell application "{app_name}" to activate'
#   subprocess.run(["osascript", "-"], input=script.encode("utf-8"), check=True)
#   script = 'tell "some application" to do something'
#   p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
#   stdout, stderr = p.communicate(script)
#   print(p.returncode, stdout, stderr)
#   os.system("osascript -e " + script)

# Example usage
# activate_window("Firefox Developer Edition", "Gemini")
#   activate_window("Safari")

Connect(False)
# Open_OpenVPN
# Add_VPN(0)

# pyautogui.moveTo(0, 0)

# OpenVPN_location = pyautogui.locateOnScreen(abs + 'OpenVPN.png', confidence=0.9)
# print(OpenVPN_location)
# if OpenVPN_location is not None:
#     OpenVPN_center = pyautogui.center(OpenVPN_location)
#     pyautogui.click(OpenVPN_center.x/2, OpenVPN_center.y/2)
#     print(OpenVPN_center.x, OpenVPN_center.y)
# else: print("OpenVPN fail")
# pyautogui.click()

# OfNoUse_locations = pyautogui.locateAllOnScreen(abs + '219.png', confidence=0.9)
# sum = 0; distance = 10; elements = []
# for element in OfNoUse_locations:
#     if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
#         elements.append(element)
# print(len(elements))
# print(sum)
