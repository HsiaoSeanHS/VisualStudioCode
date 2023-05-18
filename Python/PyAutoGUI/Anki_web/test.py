from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("https://www.google.com")

words = open('Anki_web/pending.txt')
for word in words.readlines():
    print(word)
words.close()