from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.expected_conditions import (
    url_contains,
    url_matches
)
"""
como o visibility_of_all_elements_located funciona

depois de todo l tem que ter um a,
ele vai esperar que todos os elementos sejam um a

"""
url = 'https://selenium.dunossauro.live/aula_10_c.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

link = chrome.find_element(By.CSS_SELECTOR, 'body > div > div > ul > li:nth-child(2) > a')
link.click()

# dentro da url que ele tem carregado agora contem selenium
wdw.until(url_contains('selenium'))
# verifica se a url tem http (.* -> qualquer coisa no meio) e se termina com live
wdw.until(url_contains('http.*live'))
print('contem')