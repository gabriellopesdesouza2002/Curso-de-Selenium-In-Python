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
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By



    

url = 'https://selenium.dunossauro.live/exercicio_10.html'
chrome = Chrome()

# cria o wdw         navegador     tempo_limite     frequencia de tentativa de encontrar o elemento
wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)

# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

def envia_input(driver, elemento_css, texto):
    driver.find_element(By.CSS_SELECTOR, elemento_css).send_keys(texto)
    
    
def clica_item_assim_que_disponivel(driver, locator):
    wdw.until(element_to_be_clickable(locator))
    driver.find_element(*locator).click()
    
    
    
envia_input(chrome, '#todo-name', texto='Estudar')
envia_input(chrome, '#todo-desc', texto='Estudar até amanhã')
clica_item_assim_que_disponivel(chrome, (By.CSS_SELECTOR, '#todo-submit'))

# # quando o botão estiver disponível vai clicar e dar print no nome do btn
clica_item_assim_que_disponivel(chrome, (By.CSS_SELECTOR, '#todo > div > div.buttons > button.btn.btn-primary.btn-ghost.do'))
clica_item_assim_que_disponivel(chrome, (By.CSS_SELECTOR, '#doing > div > div.buttons > button.btn.btn-primary.btn-ghost.do'))
clica_item_assim_que_disponivel(chrome, (By.CSS_SELECTOR, '#done > div > div.buttons > button'))
clica_item_assim_que_disponivel(chrome, (By.CSS_SELECTOR, '#todo > div > div.buttons > button.btn.btn-primary.btn-ghost.do'))
