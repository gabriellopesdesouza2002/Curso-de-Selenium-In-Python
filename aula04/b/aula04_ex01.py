from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_04_b.html')

caixas = chrome.find_elements(By.CLASS_NAME, 'box')
for caixa in caixas:
    caixa.click()
    sleep(.5)
else:
    for caixa in caixas:
        chrome.back()
        sleep(.5)
    else:
        for caixa in caixas:
            chrome.forward()
            sleep(.5)

print(caixas)
sleep(2)
chrome.close()