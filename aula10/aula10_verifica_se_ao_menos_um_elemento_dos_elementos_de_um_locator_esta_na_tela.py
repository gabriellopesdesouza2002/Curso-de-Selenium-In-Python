from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_any_elements_located  # se ao menos 1 elemento aparecer vai retornar true
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

locator = (By.CSS_SELECTOR, 'h1')

wdw.until(
    visibility_of_any_elements_located((locator)),
    message='Elemento Não encontrado, espera de 60s'
    ) # quero esperar que ao menos 1 elemento do locator esteja visivel 
        # qualquer h1 que aparecer vai falar (apareceu)

print('ao menos 1 h1 apareceu na page')

