from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of,  # é por elemento e não por locator (located)
    invisibility_of_element
)
from zmq import Message

url = 'https://selenium.dunossauro.live/aula_10_b.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

wdw.until(
    visibility_of(chrome.find_element_by_css_selector('body > h1:nth-child(1)')),
    message='Elemento Não encontrado, espera de 60s'
    ) # quero esperar que um determinado elemento esteja visivel 

print('h1 disponivel')

