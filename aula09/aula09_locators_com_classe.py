from functools import partial
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator
    
    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):  # se encontrar o locator, retorna True
            return True
        return False
    

url = 'https://selenium.dunossauro.live/aula_09_a.html'
chrome = Chrome()

wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)

# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

# 2 ESPERAR BOTÃO APARECER
locator = (By.CSS_SELECTOR, 'button')
esperar_button = EsperarElemento(locator)
wdw.until(method=esperar_button, message='NAO ACHEI O ELEMENTO!')  

# 3 CLICAR NO BOTÃO
chrome.find_element(By.CSS_SELECTOR, 'button').click()

# 4 ESPERAR A DIV QUE TEM O ID finished APARECER
wdw.until(method=EsperarElemento(locator=('id', 'finished')), message='NAO ACHEI O ELEMENTO!')  

# RECUPERA A DIV DE SUCESSO
div_sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')
print('A div é "Carregamento concluído"? ', div_sucesso.text == 'Carregamento concluído')

#### Qualquer dúvida vái para a página 30 da aula

