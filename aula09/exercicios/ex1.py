"""Tenho que encontrar a classe .selenium tem que 
avisar quando encontra a classe e clica no botão

"""
from functools import partial
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator
    
    def __call__(self, webdriver):
        elementos = webdriver.find_elements(*self.locator)  # Se tiver o(s) elemento(s)
        if elementos:  # se tiver os e elementos
            if 'btn-error' in elementos[0].get_attribute('class'):  # se existir selenium na classe do elemento
                return True
            else:
                return False
            
        else:
            return False 
    # return False
    

url = 'https://selenium.dunossauro.live/exercicio_09.html'
chrome = Chrome()

wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)

# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

    
esperar_button = EsperarElemento(locator=(By.CSS_SELECTOR, '#request'))  # esse locator é a localização do btn
wdw.until(method=esperar_button, message='NAO ACHEI O ELEMENTO!')
if chrome.find_element(By.CSS_SELECTOR, '#request').text == "Botão":
    print('btn-error')

# # 3 CLICAR NO BOTÃO
# chrome.find_element(By.CSS_SELECTOR, 'button').click()

# # 4 ESPERAR A classe QUE TEM O valor selenium APARECER
# wdw.until(method=EsperarElemento(locator=(By.CSS_SELECTOR, 'selenium')), message='NAO ACHEI O ELEMENTO!')  

# # RECUPERA A DIV DE SUCESSO
# div_sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')
# print('A div é "Carregamento concluído"? ', div_sucesso.text == 'Carregamento concluído')

# #### Qualquer dúvida vái para a página 30 da aula

