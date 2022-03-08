from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_all_elements_located  # só retorna true caso todos os elementos que você selecionou pelo o locator estejam disponiveis
    
)
"""
como o visibility_of_all_elements_located funciona

depois de todo l tem que ter um a,
ele vai esperar que todos os elementos sejam um a

"""
url = 'https://portal.stf.jus.br/processos/listarPartes.asp?termo=whirlpool'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

locator = (By.CSS_SELECTOR, '#tabela_processos a')

wdw.until(
    visibility_of_all_elements_located((locator)),
    message='Elementos Não encontrados, espera de 60s'
    ) # quero esperar que ao menos 1 elemento do locator esteja visivel 
        # qualquer h1 que aparecer vai falar (apareceu)

print('todos os a estão disponiveis')

