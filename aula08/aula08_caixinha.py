from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
chrome = Chrome()
url = 'https://selenium.dunossauro.live/caixinha.html'

chrome.get(url)

caixinha = chrome.find_element(By.CSS_SELECTOR, '#caixa')
p = chrome.find_element(By.CSS_SELECTOR, 'p')

ac = ActionChains(chrome)
sleep(1)

def caixa_coloria(key1, key2=None):
    ac.key_down(key1)
    if key2:  # se vinher mais um key
        ac.key_down(key2)
    ac.move_to_element(caixinha)  # foca no elemento (coloca o mouse)
    ac.click()  # clica no elemento (coloca o mouse)
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.double_click()  # clica 2x no elemento
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.move_to_element(p)  # foca no p p/ sair da caixa
    ac.key_up(key1)
    if key2:
        ac.key_down(key2)
caixa_coloria(Keys.SHIFT)
caixa_coloria(Keys.CONTROL)
caixa_coloria(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixinha)  # foca no elemento (coloca o mouse)
ac.context_click()  # clica no menu de contexto no elemento # deve ser executado fora da funcao

ac.perform()  # executa o ac