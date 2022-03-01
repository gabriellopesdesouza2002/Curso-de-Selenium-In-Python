
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pyautogui

from random import randint
chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_08_a.html'
texto = "selenium"

chrome.get(url)

textarea = chrome.find_element(By.CSS_SELECTOR, 'textarea')  # recupera o textarea

textarea.click()
sleep(1)

pyautogui.hotkey('capslock')  # ativa o caps
pyautogui.write(texto)  # escreve no textarea
pyautogui.hotkey('capslock')  # desativa o caps
