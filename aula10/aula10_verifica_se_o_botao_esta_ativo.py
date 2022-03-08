from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    staleness_of,  # só retorna true o tal elemento esteja ativo no HTML
    element_to_be_clickable
    
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
chrome = Chrome()

chrome.get(url)

tempo_espera = 60

wdw = WebDriverWait(driver=chrome, timeout=tempo_espera)


wdw.until(
    staleness_of(chrome.find_element(By.CSS_SELECTOR, 'button')),
    message=f'Elementos Não encontrados, espera de {tempo_espera}'
    ) # quero esperar que o botão proximo esteja habilitado
        # qualquer h1 que aparecer vai falar (apareceu)

print('O Botão está ativo')

chrome.find_element(By.CSS_SELECTOR, 'button').click()


