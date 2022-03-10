from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# abre o chrome
chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome = Firefox(executable_path=GeckoDriverManager().install())

wdw = WebDriverWait(chrome, 60)

# vai para o link
chrome.get('https://selenium.dunossauro.live/aula_11_d.html')

# espera o frame estar disponível quando disponível JA ENTRA NELE
wdw.until(EC.frame_to_be_available_and_switch_to_it(('name', 'iframe')))

# quando disponível...

wdw.until(EC.element_to_be_clickable(('name', 'nome')))
chrome.find_element_by_id('nome').send_keys('oi')  
