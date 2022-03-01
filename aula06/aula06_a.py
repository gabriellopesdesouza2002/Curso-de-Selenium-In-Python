from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_06_a.html'
chrome.get(url)

first_input_name = chrome.find_element_by_css_selector('input').send_keys('Gabriel Lopes')