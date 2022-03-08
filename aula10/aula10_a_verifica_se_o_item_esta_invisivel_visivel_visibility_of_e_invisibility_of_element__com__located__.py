from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,  # é por locator (located)
    invisibility_of_element_located
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

locator = (By.CSS_SELECTOR, 'body > h1:nth-child(1)')

wdw.until(
    visibility_of_element_located((locator)),
    message='Elemento Não encontrado, espera de 60s'
    ) # quero esperar que um determinado elemento esteja visivel 

print('h1 disponivel')

