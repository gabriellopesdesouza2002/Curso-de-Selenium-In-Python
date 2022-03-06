from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system

system('clear')
from random import randint
chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_09_a.html'

chrome.get(url)
chrome.minimize_window()
chrome.implicitly_wait(30)
btn = chrome.find_element(By.CSS_SELECTOR, 'button')
btn.click()

finished = chrome.find_element(By.CSS_SELECTOR, 'finished').text
print(finished == 'Carregamento concluído')