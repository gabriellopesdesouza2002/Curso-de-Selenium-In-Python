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

def primary_colors():
    """ mouse acessa o espaço de um elemento; 
        mouse clicka no elemento;
        mouse dá doubleclick no elemento
        mouse deixa o espaço de um elemento; 
        o click vem botão de contexto (direito ou esquerdo se for canhoto)
        """
    caixinha = chrome.find_element(By.CSS_SELECTOR, '#caixa')
    p = chrome.find_element(By.CSS_SELECTOR, 'p')
    ac.move_to_element(caixinha)
    ac.pause(1)
    ac.click(caixinha)
    ac.pause(1)
    ac.double_click(caixinha)
    ac.pause(1)
    ac.move_to_element(p)
    ac.pause(1)
    ac.move_to_element(caixinha)
    ac.pause(1)
    ac.perform()  # executa o ac
    chrome.refresh()
    sleep(3)
    
    
def one_key(key):
    caixinha = chrome.find_element(By.CSS_SELECTOR, '#caixa')
    p = chrome.find_element(By.CSS_SELECTOR, 'p')
    ac.key_down(key)
    ac.move_to_element(caixinha)
    ac.pause(1)
    ac.click(caixinha)
    ac.pause(1)
    ac.double_click(caixinha)
    ac.pause(1)
    ac.move_to_element(p)
    ac.pause(1)
    ac.key_up(key)
    ac.perform()  # executa o ac
    chrome.refresh()
    sleep(2)



def two_keys(key1, key2):
    caixinha = chrome.find_element(By.CSS_SELECTOR, '#caixa')
    p = chrome.find_element(By.CSS_SELECTOR, 'p')
    ac.key_down(key1)
    ac.key_down(key2)
    ac.move_to_element(caixinha)  # foca no elemento (coloca o mouse)
    ac.click()  # clica no elemento (coloca o mouse)
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.double_click()  # clica 2x no elemento
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.pause(1) # pausa o código (sem a necessidad do sleep)
    ac.move_to_element(p)  # foca no p p/ sair da caixa
    ac.key_up(key1)
    ac.key_up(key2)
    ac.perform()  # executa o ac
    chrome.refresh()
    sleep(1)



primary_colors()
sleep(1)
one_key(Keys.SHIFT)
sleep(1)
one_key(Keys.CONTROL)
sleep(1)
two_keys(Keys.SHIFT, Keys.CONTROL)
sleep(1)

ac.move_to_element(caixinha)
ac.context_click()
ac.perform()  # executa o ac