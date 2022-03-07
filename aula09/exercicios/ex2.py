"""
todo list

ao add uma tarefa, tem um delay
ao fazer a tarefa, tem um delay

criar uma tarefa
mandar para A fazer,
depois mandar para fazendo
depois mandar para Feito
e depois refaça
e PARE NO FAZENDO
"""

from functools import partial
from xml.dom.minidom import Element
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



    

url = 'https://selenium.dunossauro.live/exercicio_10.html'
chrome = Chrome()

# cria o wdw         navegador     tempo_limite     frequencia de tentativa de encontrar o elemento
wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)

# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

def envia_tarefa(driver, elemento_css, texto):
    driver.find_element(By.CSS_SELECTOR, elemento_css).send_keys(texto)
    
def clica_item(driver, btn_css):
    driver.find_element(By.CSS_SELECTOR, btn_css).click()
    
def clica_item_assim_que_disponivel(driver, btn_css):
    class EsperarElemento:
        def __init__(self, locator):
            self.locator = locator
        
        def __call__(self, webdriver):
            elementos = webdriver.find_elements(*self.locator)  # Se tiver o(s) elemento(s)
            if elementos:  # se tiver os e elementos
                return True
            else:
                return False
    
    esperar_button = EsperarElemento(locator=(By.CSS_SELECTOR, btn_css))  # esse locator é a localização do btn
    wdw.until(method=esperar_button, message='NAO ACHEI O ELEMENTO!')
    if driver.find_element(By.CSS_SELECTOR, btn_css).is_enabled:
        print(f'Clicando no botão {driver.find_element(By.CSS_SELECTOR, btn_css).text}')
        driver.find_element(By.CSS_SELECTOR, btn_css).click()
    
    
envia_tarefa(chrome, '#todo-name', texto='Estudar')
envia_tarefa(chrome, '#todo-desc', texto='Estudar até amanhã')
clica_item_assim_que_disponivel(chrome, '#todo-submit')

# quando o botão estiver disponível vai clicar e dar print no nome do btn
clica_item_assim_que_disponivel(chrome, '#todo > div > div.buttons > button.btn.btn-primary.btn-ghost.do')
clica_item_assim_que_disponivel(chrome, '#doing > div > div.buttons > button.btn.btn-primary.btn-ghost.do')
clica_item_assim_que_disponivel(chrome, '#done > div > div.buttons > button')
clica_item_assim_que_disponivel(chrome, '#todo > div > div.buttons > button.btn.btn-primary.btn-ghost.do')


    

    


# # 3 CLICAR NO BOTÃO
# chrome.find_element(By.CSS_SELECTOR, 'button').click()

# # 4 ESPERAR A classe QUE TEM O valor selenium APARECER
# wdw.until(method=EsperarElemento(locator=(By.CSS_SELECTOR, 'selenium')), message='NAO ACHEI O ELEMENTO!')  

# # RECUPERA A DIV DE SUCESSO
# div_sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')
# print('A div é "Carregamento concluído"? ', div_sucesso.text == 'Carregamento concluído')

# #### Qualquer dúvida vái para a página 30 da aula

