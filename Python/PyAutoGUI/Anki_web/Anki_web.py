
import os, time
import pyautogui, pyperclip
from PIL import Image, ImageGrab
import win32gui, win32com.client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import win32clipboard as wc
import win32con

# def CheckAdd():
#     if(win32gui.FindWindow(None, "Add") == 0):
#         os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
#         time.sleep(10)
#         shell = win32com.client.Dispatch("WScript.Shell")
#         shell.AppActivate("User 1 - Anki")
#     else: os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
#     time.sleep(3)

if win32gui.FindWindow(None, "Add") == 0 and win32gui.FindWindow(None, "User 1 - Anki") != 0: os.popen('%s%s' % ("taskkill /F /IM ","Anki.exe"))
os.system("cls")
service = Service(executable_path = "geckodriver")
driver = webdriver.Firefox(service = service)
# driver.maximize_window()
driver.set_window_position(0, 0)
driver.set_window_size(1284, 1044)

words = open('Anki_web/pending.txt', 'r')
index = words.readline().replace('\n','') #去掉換行
# while index:
# 	# print(index)
# 	index = words.readline().replace('\n','') #去掉換行
# words.close()
with open('Anki_web/pending.txt','r+') as words:
    temp = words.read()
    list = temp.split('\n')
for index in list:
    driver.get("https://dictionary.cambridge.org/zht/")
    driver.implicitly_wait(5)
    # index = "fine"

    #search_bar = driver.find_element(By.ID, "APjFqb")
    #search_button = driver.find_element(By.CLASS_NAME, "gNO89b")
    #search_bar.send_keys(word)
    #search_button.submit()
    #result_class = driver.find_element(By.CLASS_NAME, "yuRUbf")
    #result_address = result_class.find_element(By.PARTIAL_LINK_TEXT, "fine")[1]
    #driver.execute_script("arguments[0].scrollIntoView();", result_address)
    #result_address.submit()
    search_bar = driver.find_element(By.ID, "searchword")
    search_button = driver.find_element(By.CLASS_NAME, "bo.iwc.iwc-40.hao.lb0.cdo-search-button.lp-0")
    search_bar.send_keys(index)
    search_button.submit()

    Have_content = True
    try: driver.find_element(By.CSS_SELECTOR, "div.def-block.ddef_block")
    except: Have_content = False
    if Have_content: content = driver.find_element(By.CSS_SELECTOR, "div.def-block.ddef_block").text
    else: 
        print('"' + index +'" is wrong.')
        os.system("start D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/pending.txt")
        break
    # while '\n' not in content:
    # content.splitlines()
    # for i in content:
    #     if i != "\n":
    #         content = content.lstrip()
    #     elif i == "\n":
    #         content = content.lstrip()
    #         break
    # line = "\n"
    # lines = (line.strip() for line in content)
    # for line in lines:
    #     print(line)
    # right_mid_bracket = content.find("]")
    # dontknow = content[right_mid_bracket+1]
    # if dontknow == '\n': print("_")
    # print(dontknow, type(dontknow))
    # if right_mid_bracket != -1: content = content[right_mid_bracket+2:] 
    OfNoUse = True
    content = content[content.find("\n") + 1:] 
    try: driver.find_element(By.CSS_SELECTOR, "span.epp-xref.dxref")
    except: OfNoUse = False
    if OfNoUse: content = content[content.find("\n") + 1:] #無用資訊
    try: driver.find_element(By.CSS_SELECTOR, "span.def-info.ddef-info.gc.dgc")
    except: OfNoUse = False
    if OfNoUse: content = content[content.find("\n") + 1:] #無用資訊
    count = 0; start = 0 #content.find('\n') + 1  # Find the position of the second '\n'
    print(content)
    while count >= 0:
        n = content.find("\n",start)
        if n == -1: break
        else: count += 1
        if count % 2 == 1: content = content[:n] + " " + content[n+1:]
        elif count > 0: content = content[:n+1] + "-" + content[n+1:]
        start = n + 1
    part_of_speech = driver.find_element(By.CSS_SELECTOR, "span.pos.dpos").text
    # part_of_speech = part_of_speech.title()
    # print(part_of_speech)
    content = part_of_speech + ".\n" + content
    print(content)

    phoneme = driver.find_element(By.CSS_SELECTOR, "span.us.dpron-i span.ipa.dipa.lpr-2.lpl-1").text
    print(phoneme)

    Source = driver.current_url
    print(Source)

    #Cloze

    Cloze_A = index + "{{c20::}}{{c220::}}{{c320::}}"
    Cloze_B = index[0] + "{{c50::" + index[1:-1] + "}}" + index[-1]
    Cloze_C = index[0] + "{{c150::" + index[1:-1] + "}}" + index[-1]
    # print(Cloze_A, Cloze_B, Cloze_C)
    pyautogui.PAUSE = 0.5
    if win32gui.FindWindow(None, "Add") == 0:
        if win32gui.FindWindow(None, "User 1 - Anki") != 0: os.popen('%s%s' % ("taskkill /F /IM ","Anki.exe"))
        os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
        time.sleep(10)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("User 1 - Anki")
    Anki = win32gui.FindWindow(None, "User 1 - Anki")
    os.system("cls")
    if Anki != 0:
        Add_home_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/Add_home.png', confidence=0.9)
        New_Learn_Due_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/New_Learn_Due.png', confidence=0.9)
        if Add_home_location and New_Learn_Due_location is not None:
            Add_home_center = pyautogui.center(Add_home_location)
            pyautogui.click(Add_home_center.x, Add_home_center.y)
            English_Deck_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/English_Deck.png', confidence=0.9)
            if English_Deck_location is not None:
                English_Deck_center = pyautogui.center(English_Deck_location)
                pyautogui.click(English_Deck_center.x, English_Deck_center.y)
                pyautogui.typewrite(['a', 'd', 'd'])
            Choose_Deck_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/Choose_Deck.png', confidence=0.9)
            if Choose_Deck_location is not None:
                Choose_Deck_center = pyautogui.center(Choose_Deck_location)
                pyautogui.click(Choose_Deck_center.x, Choose_Deck_center.y)
            Index_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/Index.png', confidence=0.9)
        if Index_location is not None:
            Index_center = pyautogui.center(Index_location)
            pyautogui.click(Index_center.x, Index_center.y)


        pyautogui.typewrite(index)
        pyautogui.press('tab')
        pyperclip.copy(content)
        pyautogui.hotkey('ctrl', 'v')
        # pyautogui.typewrite(content)
        pyautogui.press('tab', presses=3)
        pyperclip.copy(phoneme)
        pyautogui.hotkey('ctrl', 'v')
        # pyautogui.typewrite(phoneme)
        pyautogui.press('tab')

        #image
        # pyautogui.hotkey('ctrl', 't', interval=0.1)
        # driver.switch_to.window(driver.window_handles[1])

        driver.get("https://www.google.com.tw/imghp?hl=zh-TW&authuser=0&ogbl")
        search_bar = driver.find_element(By.ID, "APjFqb")
        search_button = driver.find_element(By.CSS_SELECTOR, "span.z1asCe.MZy1Rb")
        search_bar.send_keys(index)
        search_button.submit()
        # previous = ""
        # while True:
        #     wc.OpenClipboard()
        #     try:
        #         image = wc.GetClipboardData(win32con.CF_DIB)
        #     except TypeError:
        #         # Ignore unsupported data types
        #         # os.system("cls")
        #         print("waiting for 10 seconds")
        #         wc.CloseClipboard()
        #         time.sleep(10)
        #         continue
        #     if image != previous:
        #         wc.EmptyClipboard()
        #         break
        #     time.sleep(0.1)
        #     wc.CloseClipboard()
        pyperclip.waitForNewPaste()
        ImageGrab.grabclipboard()
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab', presses=2)
        pyautogui.typewrite(Source)
        pyautogui.press('tab', presses=6)
        pyautogui.typewrite(Cloze_A)
        pyautogui.press('tab', presses=2)
        pyautogui.typewrite(Cloze_B)
        pyautogui.press('tab', presses=2)
        pyautogui.typewrite(Cloze_C)
        Add_main_location = pyautogui.locateOnScreen('D:/Backup/VisualStudioCode/Python/PyAutoGUI/Anki_web/screenshots/Add_main.png', confidence=0.9)
        if Add_main_location is not None:
            Add_main_center = pyautogui.center(Add_main_location)
            pyautogui.click(Add_main_center.x, Add_main_center.y)
    else:
        print("Anki open fail")
driver.quit()
if win32gui.FindWindow(None, "Add") != 0:
    pyautogui.hotkey('alt', 'f4')
    os.popen('%s%s' % ("taskkill /F /IM ","Anki.exe"))
print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))