from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_04_a.html')
sleep(1)

url_parser = urlparse(chrome.current_url)
