from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.expected_conditions import (
    title_contains,
    title_is
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

link = chrome.find_element(By.CSS_SELECTOR, 'body > div > div > ul > li:nth-child(1) > a')
link.click()

# titulo da page -> Aula 10b

# contem aula no titulo
wdw.until(title_contains('Aula'))
print('contem')
# verifica se o titulo é igual ao da pagina atual
wdw.until(title_is('selenium'))
print('é igual')