import os, time, random, pydub, urllib
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def rand(last): return random.randint(0, last)
def human(): driver.implicitly_wait(random.randint(2,3))
def u(n, l):  return l.upper() if(n%2) else l
def t(x, l, n): n += 1; return x + u(n, l) + str(n), n
def AcPw(Service):
    PAs = open("D:/PA.txt", "r")
    lines = PAs.readlines()
    PAs.close()
    for line in lines:
        line = line.replace("\n", "")
        if line.find("Email") == 0: email = line.split(" ")[1]
        if line.find(Service) == 0: passwd = line.split(" ")[1]
    return email, passwd

Mozilla = "Mozilla/5.0 "
System = ["(Windows NT 10.0; Win64; x64) ",
          "(X11; Linux x86_64) ",
          "(Macintosh; Intel Mac OS X 10_15_7) ",
          "(Macintosh; Intel Mac OS X 13_1) "]
AppleWebKit = ["AppleWebKit/537.36 (KHTML, like Gecko) ",
               "AppleWebKit/605.1.15 (KHTML, like Gecko) ",
               "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 "]
Chrome = ["Chrome/108.0.0.0 ",
          "Chrome/109.0.0.0 "]
Safari = ["Safari/537.36",
          "Safari/605.1.15"]
id, B = AcPw("Bahamut")
id = id[:11]; p = a = ""; n = 0
for l in id[5:9]: p, n = t(p, l, n)
for l in B[::2]: a, n = t(a, l, n)
R = "user"; I = "id"; S = "pass"; W = "word"; pa = p + a; Ar = rand(2)
Agent = Mozilla + System[rand(3)] + AppleWebKit[Ar] + (Chrome[rand(1)] if Ar != 2 else "") + Safari[rand(1)]
options = Options()
options.set_preference("general.useragent.override", Agent)
service = Service(executable_path = "geckodriver")
driver = webdriver.Firefox(service = service, options = options)

os.system("cls")
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/temp."
driver.get("https://user.gamer.com.tw/login.php"); human
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "g-recaptcha").find_elements(By.TAG_NAME, "iframe")[0]); human
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[3]/div[4]").find_elements(By.TAG_NAME, "iframe")[0])

try:
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "recaptcha-audio-button").click()
    try:
        src = driver.find_element(By.ID, "audio-source").get_attribute("src")
        urllib.request.urlretrieve(src, abs + "mp3")
        sound = pydub.AudioSegment.from_mp3(abs + "mp3")
        sound.export(abs + "wav", format = "wav")
        sample_audio = sr.AudioFile(abs + "wav")
        print("Get sound file successfully.")
        try:
            r = sr.Recognizer()
            with sr.WavFile(abs + "wav") as source: audio = r.listen(source)
            key = r.recognize_google(audio)
            try: 
                human
                driver.find_element(By.ID, "audio-response").send_keys(key.lower())
                driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
            except: print("Cannot find audio input.")
        except Exception as e: print("Sound recongnize failed:" + e)
        try: 
            os.remove(abs + "mp3"); os.remove(abs + "wav")
            print("Temp file deleted.") # The last step in anticipation.
        except: print("Temp sound files are not exist.")
    except: print("Cannot doing audio test.")
except: print("No reCAPTCHA")

driver.switch_to.default_content()
driver.find_element(By.NAME, R + I).send_keys(id)
driver.find_element(By.NAME, S + W).send_keys(pa)

while True:
    try:
        driver.find_element(By.LINK_TEXT, "登入").click()
        human
        driver.find_element(By.ID, "signin-btn")
        break
    except: continue
driver.find_element(By.ID, "signin-btn").click() # 每日簽到
try: driver.find_element(By.CSS_SELECTOR, 'button.popup-dailybox__btn').click() # 領取雙倍巴幣
except: print("已簽到")
time.sleep(15)
driver.quit()