from selenium.webdriver import Chrome
from time import sleep
from random import randint

chrome = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_07_d.html'
chrome.get(url)

# # da foco / ativa o focus
# chrome.find_element_by_css_selector('input').send_keys('Gabriel')

# # tira o focus no elemento input e 
# chrome.find_element_by_css_selector('[onload]').click()

for i in range(100):  # vai consumir o range
    chrome.find_element_by_css_selector('input').send_keys(randint(0, 1))
    # sleep()
    chrome.find_element_by_css_selector('p').click()


