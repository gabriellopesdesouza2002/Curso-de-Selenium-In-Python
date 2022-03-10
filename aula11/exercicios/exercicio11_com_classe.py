"""
https://selenium.dunossauro.live/exercicio_12.html

preencher o form por meio dos prompts
depois que enviar, pegar o popup e validar as infos dele com as suas
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

class PreencheFormAlert:    
    def __init__(self, url='https://selenium.dunossauro.live/exercicio_12.html'):
        # abre o firefox
        self.firefox = Firefox(executable_path=GeckoDriverManager().install())     
        self.get = self.firefox.get(url)
        self.wdw = WebDriverWait(self.firefox, 60)

    def espera_elemento_disponivel_e_clica(self, locator: tuple):
        # espera o item estar disponível quando disponível JA ENTRA NELE
        self.wdw.until(EC.element_to_be_clickable(locator))
        # clica no elemento
        self.firefox.find_element(*locator).click()
        # vai para o link

    def espera_pelo_alert_e_envia_send_keys_e_aceita_alert(self, your_send_keys: str='Seu valor'):
        # espera pelo alerta e da um switch para ele automaticamente
        alerta = self.wdw.until(EC.alert_is_present())
        alerta.send_keys(your_send_keys)  # envia para o alerta o nome
        alerta.accept()  # aceita o alerta
        
    
    def verifica_se_abriu_x_janelas_e_muda_para_a_ultima_janela(self, num_de_janelas: int=2):
        # verifica se abriu x numeros de janelas
        print(f'Você está na janela -> {self.firefox.current_window_handle}')
        self.wdw.until(EC.number_of_windows_to_be(num_de_janelas))
        print(f'Agora, você tem {len(self.firefox.window_handles)} janelas abertas')
        todas_as_windows = self.firefox.window_handles
        self.firefox.switch_to.window(todas_as_windows[-1])
        print(f'Agora, você está na janela -> {self.firefox.current_window_handle}')
        
    def espera_e_recupera_textos_de__varios_elementos(self, locator: tuple):
        import os
        os.system('clear')
        self.wdw.until(EC.element_to_be_clickable(locator))
        elementos_selenium = self.firefox.find_elements(*locator)
        elementos_texts = [texto.text for texto in elementos_selenium]
        for elemento in elementos_texts:
            print(elemento)

    def fecha_navegador(self):
        self.firefox.quit()
        
firefox = PreencheFormAlert()
firefox.espera_elemento_disponivel_e_clica(locator=(By.CSS_SELECTOR, 'input[name=nome]'))
firefox.espera_pelo_alert_e_envia_send_keys_e_aceita_alert('Gabriel')
firefox.espera_elemento_disponivel_e_clica(locator=(By.CSS_SELECTOR, 'input[name=email]'))
firefox.espera_pelo_alert_e_envia_send_keys_e_aceita_alert('gabriel@gmail.com')
firefox.espera_elemento_disponivel_e_clica(locator=(By.CSS_SELECTOR, 'input[name=signo]'))
firefox.espera_pelo_alert_e_envia_send_keys_e_aceita_alert('nao tenho ja falei')
firefox.espera_elemento_disponivel_e_clica(locator=(By.CSS_SELECTOR, 'input[value=Enviar]'))
firefox.verifica_se_abriu_x_janelas_e_muda_para_a_ultima_janela()
firefox.espera_e_recupera_textos_de__varios_elementos((By.CSS_SELECTOR, 'h1'))
firefox.fecha_navegador()

