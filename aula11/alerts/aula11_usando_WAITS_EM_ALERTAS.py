from time import sleep
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# ALERT
from selenium.webdriver.common.alert import Alert

chrome = Firefox(executable_path=GeckoDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_a.html')
        

wdw = WebDriverWait(chrome, timeout=30)
wdw.until(EC.element_to_be_clickable(locator=(By.CSS_SELECTOR, '#alertd')))  # aguarda o elemento ser clicavel
elemento = chrome.find_element(By.CSS_SELECTOR, '#alertd')
elemento.click()

alerta = wdw.until(EC.alert_is_present())  # vai para o alerta e espera por ele
alerta.accept() 

