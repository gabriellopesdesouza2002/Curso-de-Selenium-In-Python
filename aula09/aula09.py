from functools import partial
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class EsperarElementoAtivo:  # vai ter problema pq o Wait não identificavel se é ativo ou não para isso tem a função abaixo
  # espera baseada em classe
    def __init__(self, locator):
        self.locator = locator
    
    def __call__(self, webdriver):
        elementos = webdriver.find_elements(*self.locator)  # Se tiver o(s) elemento(s)
        if elementos:  # se tiver os e elementos
            return 'unclick' in elementos[0].get_attribute('class')  # se existir unclick na classe do elemento
        return False
    
def esperar_elemento(by, elemento, webdriver):  # espera baseada em função
    if webdriver.find_elements(by, elemento):
        return True
    return False
    

url = 'https://selenium.dunossauro.live/aula_09.html'
chrome = Chrome()

wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)

# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

# 2 ESPERAR BOTÃO APARECER
locator = (By.CSS_SELECTOR, 'button')
esperar_button = EsperarElementoAtivo(locator)
wdw.until_not(method=esperar_button, message='NAO ACHEI O ELEMENTO!')  

# 3 CLICAR NO BOTÃO
chrome.find_element(By.CSS_SELECTOR, 'button').click()

# 4 ESPERAR A DIV QUE TEM O ID finished APARECER
wdw.until(method=partial(esperar_elemento, 'id', 'finished'), message='NAO ACHEI O ELEMENTO!')  

# RECUPERA A DIV DE SUCESSO
div_sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')
print('A div é "Carregamento concluído"? ', div_sucesso.text == 'Carregamento concluído')


