"""
Preencher o form com waits prontos
"""

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element_value,
)

class FormSubmitGo():
    def __init__(self, url='https://selenium.dunossauro.live/aula_10_d.html'):
        self.chrome = Chrome()
        self.url = url
        
    def ver_por_value(self):
        self.chrome.get(self.url)
        wdw = WebDriverWait(driver=self.chrome, timeout=60)

        """Saber se o elemento (pedaço de texto) está presente no elemento"""


        """LOCATORS"""
        locator_nome = (By.CSS_SELECTOR, 'input[name=nome]')
        locator_email = (By.CSS_SELECTOR, 'input[name=email]')
        locator_confirma_email = (By.CSS_SELECTOR, 'input[name=c_email]')
        locator_senha = (By.CSS_SELECTOR, 'input[name=senha]')
        locator_confirma_senha = (By.CSS_SELECTOR, 'input[name=c_senha]')
        locator_submit = (By.CSS_SELECTOR, 'input[name=button]')



        # quero esperar que o value esteja presente desse elemento
        # o texto do value tem que estar presente no texto que enviamos pelo par -> text_
        wdw.until(text_to_be_present_in_element_value(locator=locator_nome, text_='disponível'))  # quando estiver "disponível" no value do input nome...
        self.chrome.find_element(*locator_nome).send_keys('gabriel')  # ESCREVE NO INPUT NOME

        wdw.until(text_to_be_present_in_element_value(locator=locator_email, text_='disponível'))  # quando estiver "disponível" no value do input email...
        self.chrome.find_element(*locator_email).send_keys('gabriel@gmail.mail.com')  # ESCREVE NO INPUT email

        wdw.until(text_to_be_present_in_element_value(locator=locator_confirma_email, text_='disponível'))  # quando estiver "disponível" no value do input c_email...
        self.chrome.find_element(*locator_confirma_email).send_keys('gabriel@gmail.mail.com')  # ESCREVE NO INPUT NOME

        wdw.until(text_to_be_present_in_element_value(locator=locator_senha, text_='disponível'))  # quando estiver "disponível" no value do input nome...
        self.chrome.find_element(*locator_senha).send_keys('bolabola')  # ESCREVE NO INPUT NOME

        wdw.until(text_to_be_present_in_element_value(locator=locator_confirma_senha, text_='disponível'))  # quando estiver "disponível" no value do input nome...
        self.chrome.find_element(*locator_confirma_senha).send_keys('bolabola')  # ESCREVE NO INPUT NOME

        wdw.until(text_to_be_present_in_element_value(locator=locator_submit, text_='disponível'))  # quando estiver "disponível" no value do input nome...
        self.chrome.find_element(*locator_submit).click()  # ESCREVE NO INPUT NOME
        
chrome = FormSubmitGo()
chrome.ver_por_value()