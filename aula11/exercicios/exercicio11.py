"""
https://selenium.dunossauro.live/exercicio_12.html

preencher o form por meio dos prompts
depois que enviar, pegar o popup e validar as infos dele com as suas
"""

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# abre o chrome
chrome = Chrome(executable_path=ChromeDriverManager().install())
# chrome = Firefox(executable_path=GeckoDriverManager().install())

wdw = WebDriverWait(chrome, 60)

# vai para o link
chrome.get('https://selenium.dunossauro.live/exercicio_12.html')

# espera o item estar disponível quando disponível JA ENTRA NELE
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=nome]')))

# clica no nome
chrome.find_element(By.CSS_SELECTOR, 'input[name=nome]').click()


alerta = wdw.until(EC.alert_is_present())  # vai para o alerta e espera por ele
alerta.accept() 



# quando disponível...

wdw.until(EC.element_to_be_clickable(('name' 'nome')))
chrome.find_element_by_id('nome').send_keys('oi')  
