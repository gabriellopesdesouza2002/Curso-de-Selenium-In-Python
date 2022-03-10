from time import sleep
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# ALERT
from selenium.webdriver.common.alert import Alert

class Classe:
    def __init__(self, url='https://selenium.dunossauro.live/aula_11_a.html'):
        self.chrome = Firefox(executable_path=GeckoDriverManager().install())
        self.get = self.chrome.get(url)
        
        
    def clica_elemento_quando_disponivel(self, locator):
        wdw = WebDriverWait(driver=self.chrome, timeout=30)
        wdw.until(EC.element_to_be_clickable(locator=locator))  # aguarda o elemento ser clicavel
        elemento = self.chrome.find_element(*locator)
        elemento.click()
        sleep(1)

    def muda_p_alerta_e_clica_em_accept(self):
        alerta = self.chrome.switch_to.alert
        alerta.send_keys('oi')
chrome = Classe()
chrome.clica_elemento_quando_disponivel(locator=(By.CSS_SELECTOR, '#prompt'))
chrome.muda_p_alerta_e_clica_em_accept()    