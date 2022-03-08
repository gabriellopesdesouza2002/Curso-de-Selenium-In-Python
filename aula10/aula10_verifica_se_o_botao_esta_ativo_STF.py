from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    staleness_of  # só retorna true o tal elemento esteja ativo no HTML
    
)

url = 'https://portal.stf.jus.br/processos/listarPartes.asp?termo=whirlpool'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)


wdw.until_not(
    staleness_of((chrome.find_element(By.CSS_SELECTOR, '#paginacao-proxima-pagina span'))),
    message='Elementos Não encontrados, espera de 60s'
    ) # quero esperar que o botão proximo esteja habilitado
        # qualquer h1 que aparecer vai falar (apareceu)

print('O Botão está ativo')

