import warnings
warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True, defaulting to execution_context_id")

import os
import json
import asyncio
import subprocess

from applescript import AppleScript
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from solver.recaptchaSolver import solver

def u(n, l):  return l.upper() if(n%2) else l
def t(x, l, n): n += 1; return x + u(n, l) + str(n), n
def AcPw(Service):
    bahamut_path = os.path.join(os.path.expanduser("~"), ".bahamut.json")
    with open(bahamut_path) as f:
        bahamut = json.load(f)
    email = bahamut["email"]
    passwd = bahamut[Service]
    return email, passwd

id, B = AcPw("Bahamut")
id = id[:11]; p = a = ""; n = 0
for l in id[5:9]: p, n = t(p, l, n)
for l in B[::2]: a, n = t(a, l, n)
R = "user"; I = "id"; S = "pass"; W = "word"; pa = p + a 

async def close_all_chrome():
    try:
        # Kill all selenium-driverless Chrome processes
        os.system('pkill -f "selenium_driverless" 2>/dev/null')
        os.system('pkill -f "Google Chrome.*remote-debugging-port" 2>/dev/null')
        
        # Also try AppleScript for any regular Chrome instances
        AppleScript('''
                        if application "Google Chrome" is running then
                            tell application "Google Chrome" to quit
                        end if
                    ''').run()
        
        # Wait a moment for processes to terminate
        await asyncio.sleep(2)
        
        # Clean up selenium-driverless cache directory
        selenium_cache_dir = os.path.expanduser('~/Library/Application Support/selenium-driverless')
        if os.path.exists(selenium_cache_dir):
            try:
                import shutil
                shutil.rmtree(selenium_cache_dir)
                # print("Cleaned selenium-driverless cache directory")
            except Exception as e:
                print(f"Warning: Could not clean cache directory: {e}")
        
        # Recreate the directory to avoid FileNotFoundError
        try:
            os.makedirs(selenium_cache_dir, exist_ok=True)
        except Exception as e:
            print(f"Warning: Could not recreate cache directory: {e}")
        
        # Clean up any leftover selenium temp directories
        os.system('rm -rf /tmp/selenium_driverless_* 2>/dev/null')
        os.system('rm -rf /var/folders/*/T/selenium_driverless_* 2>/dev/null')
        
        # Force garbage collection to free up resources
        import gc
        gc.collect()
        
    except Exception as e:
        print(f"Warning: Error closing Chrome processes: {e}")
        pass

    try:
        subprocess.run(['pkill', '-f', 'selenium_driverless'], capture_output=True)
        subprocess.run(['rm', '-rf', '/tmp/selenium_driverless_*'], shell=True, capture_output=True)
    except:
        pass

async def submit_recaptcha_token(driver, token):
    """
    Submit the reCAPTCHA token directly to the page
    """
    script = f"""
    // Set the token in the hidden textarea
    var responseField = document.getElementById('g-recaptcha-response');
    if (responseField) {{
        responseField.innerHTML = '{token}';
        responseField.value = '{token}';
    }}
    
    // Override grecaptcha.getResponse to return our token
    if (typeof grecaptcha !== 'undefined') {{
        grecaptcha.getResponse = function() {{ return '{token}'; }};
    }}
    
    // Trigger callback if it exists
    if (window.recaptchaCallback) {{
        window.recaptchaCallback('{token}');
    }}
    """
    await driver.execute_script(script)

async def login(driver):
    await driver.get("https://user.gamer.com.tw/login.php", wait_load=True)
    
    try:
        # Get current page URL for the reCAPTCHA solver
        current_url = await driver.current_url
        print(f"Solving reCAPTCHA for: {current_url}")
        
        # Use your recaptchaSolver to get the token
        data = solver(current_url)
        recaptcha_token = data['recaptcha_token']
        print(f"reCAPTCHA solved successfully! Token received.")
        
        # Apply cookies if provided by the solver
        if 'cookies' in data:
            for cookie in data['cookies']:
                try:
                    await driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Warning: Could not add cookie: {e}")
        
        # Submit the reCAPTCHA token
        await submit_recaptcha_token(driver, recaptcha_token)
        print("reCAPTCHA token submitted successfully!")
        
    except Exception as e:
        print(f"Error solving reCAPTCHA with token method: {e}")
        print("Falling back to manual method...")
        
        # Fallback to manual clicking method
        try:
            grecaptcha = await driver.find_element(By.CLASS_NAME, "g-recaptcha")
            grecaptcha_iframe = await grecaptcha.find_element(By.TAG_NAME, "iframe")
            await driver.switch_to.frame(grecaptcha_iframe)
            grecaptcha_check = await driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")
            await grecaptcha_check.click()
            await driver.sleep(30)  # Give time for manual solving
            await driver.switch_to.default_content()
        except Exception as manual_error:
            print(f"Manual method also failed: {manual_error}")
            raise
    
    # Fill in login credentials
    account = await driver.find_element(By.XPATH, "/html/body/div[3]/div[4]")
    account_iframe = await account.find_element(By.TAG_NAME, "iframe")
    await driver.switch_to.frame(account_iframe)
    await driver.find_element(By.NAME, R + I).send_keys(id)
    await driver.find_element(By.NAME, S + W).send_keys(pa)
    
    # Submit login form
    while True:
        try:
            await driver.find_element(By.LINK_TEXT, "登入").click()
            await driver.find_element(By.ID, "signin-btn")
            break
        except: 
            pass

async def DailySignin():
    await close_all_chrome()

    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    # options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--max_old_space_size=4096")
    options.add_argument("--disable-features=TranslateUI")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-dns-prefetch")
    options.add_argument("--disable-dns-over-https")
    options.add_argument("--dns-prefetch-disable")
    
    try:
        async with webdriver.Chrome(options=options) as driver:
            # os.system('cls') # Windows
            os.system('clear')  # Linux/Mac
            await login(driver)
            # await 
    except Exception as e:
        print(f"Error running DailySignin automation: {e}")
        raise

    await close_all_chrome()

asyncio.run(DailySignin())