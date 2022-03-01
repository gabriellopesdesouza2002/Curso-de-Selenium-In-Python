from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_05_c.html')
sleep(1)


filme = chrome.find_element_by_name('filme')
email = chrome.find_element_by_name('email')
telefone = chrome.find_element_by_name('telefone')
submit = chrome.find_element_by_name('enviar')

filme.send_keys('Jesus Cristo É o Senhor!')
email.send_keys('bolarede792@gmail.com')
telefone.send_keys('(011)987654321')
submit.click()