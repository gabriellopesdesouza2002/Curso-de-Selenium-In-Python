from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener, 
    EventFiringWebDriver
) # pega o suporte (apoio) para eventos

from time import sleep
from random import choice, randint

class Escuta(AbstractEventListener):  # a classe traz as caracteristicas do AbstractEventListener (escuta de eventos)
    def before_click(self, elemento, webdriver):  # ANTES DO CLICK
        if elemento.tag_name == 'label':  # se A TAG DO ELEMENTO QUE FOI CLICADO É UM label
            print(f'Valor do {elemento.tag_name} ANTES do click -> {elemento.text}') # MOSTRA O VALOR DO SPAN DO NOME



               
    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'label':  # se A TAG DO ELEMENTO QUE FOI CLICADO É UM label
            print(f'Valor do {elemento.tag_name} DEPOIS do click -> {elemento.text}') # MOSTRA O VALOR DO SPAN DO NOME


chrome = Chrome()

rap10 = EventFiringWebDriver(chrome, Escuta())  # disparador de eventos pegou o chrome e juntou com a Escuta()
# o EventFiringWebDriver constroi um "wrapper" (um empacotador)

rap10.get('https://curso-python-selenium.netlify.app/aula_07.html') #foi pro site
sleep(2)
nome_input = rap10.find_element(By.XPATH, '//*[(@id = "nome")]')  # recuperou o input
label_input = rap10.find_element(By.CSS_SELECTOR, "#lnome")  # recuperou o label do input que É O Q VAI MUDAR
label_input.click()  # CLICOU NO INPUT
nome_input.send_keys("Gabriel")


email_input = rap10.find_element(By.XPATH, '//*[(@id = "email")]')
label_input_email = rap10.find_element(By.CSS_SELECTOR, "#lemail")
label_input_email.click()
email_input.send_keys("badf@gas.com")

senha_input = rap10.find_element(By.XPATH, '//*[(@id = "senha")]')
label_input_senha = rap10.find_element(By.CSS_SELECTOR, "#lsenha")
label_input_senha.click()
senha_input.send_keys("4321")

input_envio = chrome.find_element(By.XPATH, '//*[@id="btn"]')
label_input_envio = rap10.find_element(By.CSS_SELECTOR, "#lbtn")
input_envio.click()

chrome.quit()