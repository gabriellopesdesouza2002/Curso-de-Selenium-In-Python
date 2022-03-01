from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_04_a.html')
lista_n_ordenada = chrome.find_element(By.TAG_NAME, 'ul')
lis = lista_n_ordenada.find_elements(By.TAG_NAME, 'li')

for li in lis:
    li_object = li.find_element(By. TAG_NAME, 'a')
    link = li_object.get_attribute('href')
    
    print(link, li_object.text)
chrome.close()