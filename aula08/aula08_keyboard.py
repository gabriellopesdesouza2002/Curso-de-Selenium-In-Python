from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


chrome = Chrome()
url = 'https://selenium.dunossauro.live/keyboard.html'
chrome.get(url)
sleep(1)

chrome.find_element(By.CSS_SELECTOR, 'html').send_keys('Selenium')
