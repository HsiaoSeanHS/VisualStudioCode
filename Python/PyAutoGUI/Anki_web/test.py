from selenium import webdriver
import chardet

driver = webdriver.Firefox()
# driver.get("https://www.google.com")

#words = open('Anki_web/pending.txt')
#for word in words.readlines():
#    print(word)
#words.close()
text = open('Anki_web/KK.txt', 'rb').read()
print(chardet.detect(text))
print(text)
print(text.decode('iso-8859-9').encode('utf8'))
driver.close()