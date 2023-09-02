import os, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
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
def randAgent():
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
    Ar = rand(2)
    return Mozilla + System[rand(3)] + AppleWebKit[Ar] + (Chrome[rand(1)] if Ar != 2 else "") + Safari[rand(1)]

id, G = AcPw("GODLIKE")
p = a = ""; n = 0
for l in id[5:9]: p, n = t(p, l, n)
for l in G: a, n = t(a, l, n) if l.isupper() else (a, n)
R = "user"; I = "name"; S = "pass"; W = "word"; pa = p + a; pa = p + a
Agent = randAgent()
options = Options()
options.set_preference("general.useragent.override", Agent)
driver = webdriver.Firefox(options = options)

os.system("cls")
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/temp."
driver.maximize_window()
driver.get("https://panel.godlike.host/auth/login")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "LoginContainer___StyledP2-sc-qtrnpk-2.dsbbAC").click()
driver.find_element(By.NAME, R + I).send_keys(id)
driver.find_element(By.NAME, S + W).send_keys(pa)
driver.find_element(By.CLASS_NAME, "Button__ButtonStyle-sc-1qu1gou-0.iCUqGO").click()
while driver.find_element(By.ID, "btnLogin") is None: time.sleep(1)
driver.find_element(By.NAME, R + I).send_keys(id)
driver.find_element(By.NAME, S + W).send_keys(pa)
driver.find_element(By.ID, "btnLogin").click()
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "ServerRow___StyledSpan-sc-1ibsw91-3.eABDrG").click()
driver.find_element(By.CLASS_NAME, "style-module_4LBM1DKx.style-module_3kBDV_wo.style-module_KhQ5Q8AB.style-module_AOuopO_r") # Start
time.sleep(30)
while True:
    while driver.find_element(By.CLASS_NAME, "Button___StyledSpan-sc-1qu1gou-2") is None: time.sleep(60)
    driver.find_element(By.CLASS_NAME, "Button___StyledSpan-sc-1qu1gou-2").click()
    print(driver.find_element(By.CLASS_NAME, "ServerConsole___StyledDiv14-sc-13p0yj4-24.blaIvP").text.split("in ")[1].split("A")[0])
    time.sleep(300)
