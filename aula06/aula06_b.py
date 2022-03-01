from tkinter import Button
from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_06_a.html'
chrome.get(url)

first_input_name = chrome.find_element_by_css_selector('[name="nome"]').send_keys('Gabriel Lopes')
secound_input_password = chrome.find_element_by_css_selector('[name="senha"]').send_keys('IRINEU')
btn = chrome.find_element_by_css_selector('[name="l0c"]').click()