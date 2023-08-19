
import os, time, random, pydub, urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import speech_recognition as sr

def delay():
    time.sleep(random.randint(2,3))
def u(n, l): 
    if(n%2): return l.upper() 
    else: return l
def t(x, l, n):
    n += 1
    return x + u(n, l) + str(n), n

# profile = webdriver.FirefoxProfile()
options=Options()
# options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
service = Service(executable_path = "geckodriver")
driver = webdriver.Firefox(service = service) # , options = options

os.system("cls")
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/temp."
driver.get("https://user.gamer.com.tw/login.php")

driver.implicitly_wait(5)
reCAPTCHA = driver.find_element(By.CLASS_NAME, "g-recaptcha")
frames = reCAPTCHA.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[0])
delay()
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

driver.switch_to.default_content()
frames = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]").find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[0])

try:
    delay()
    driver.find_element(By.ID, "recaptcha-audio-button").click()

    while True:
        try:
            src = driver.find_element(By.ID, "audio-source").get_attribute("src")
            urllib.request.urlretrieve(src, abs + "mp3")
            sound = pydub.AudioSegment.from_mp3(abs + "mp3")
            sound.export(abs + "wav", format = "wav")
            sample_audio = sr.AudioFile(abs + "wav")

            r = sr.Recognizer()
            with sr.WavFile(abs + "wav") as source: audio = r.listen(source)
            key = r.recognize_google(audio)
            print("[INFO] Recaptcha Passcode: %s"%key)

            delay()
            driver.find_element(By.ID, "audio-response").send_keys(key.lower())
            driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
            break
        except:
            try: 
                driver.find_element(By.LINK_TEXT, "登入")
                break
            except: pass
            print("Try again.")
            driver.implicitly_wait(1)
            continue
except:
    print("No reCAPTCHA")

driver.switch_to.default_content()

id = "Hsiao Sean H.S."; B = "Bahamut"; p = a = ""; n = 0
for l in id[6:10].lower(): p, n = t(p, l, n)
for l in B[::2]: a, n = t(a, l, n)
        
r = "user"; i = "id"; s = "pass"; w = "word"; pa = p + a
id_bar = driver.find_element(By.NAME, r + i)
pa_bar = driver.find_element(By.NAME, s + w)
id_bar.send_keys(id.replace(" ", "").lower().replace(".", ""))
pa_bar.send_keys(pa)
while True:
    try:
        driver.find_element(By.LINK_TEXT, "登入").click()
        break
    except:
        delay()
        continue

print("Done.")