"""
Preencher o form com waits prontos
"""

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element_value,
    text_to_be_present_in_element
)

class FormSubmitGo():
    def __init__(self, url='https://selenium.dunossauro.live/exercicio_11.html'):
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

        def executa():
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
            
            exit()
        # quero esperar que o value esteja presente desse elemento
        # o texto do value tem que estar presente no texto que enviamos pelo par -> text_
        try:
            executa()
        except Exception:
            self.chrome.refresh()
            executa()
            
    def ver_por_text(self):
        self.chrome.get(self.url)

        def executa():
            wdw = WebDriverWait(driver=self.chrome, timeout=60)

            """Saber se o elemento (pedaço de texto) está presente no elemento"""


            """LOCATORS"""
            locator_nome = (By.CSS_SELECTOR, 'input[name=nome]')
            locator_email = (By.CSS_SELECTOR, 'input[name=email]')
            locator_confirma_email = (By.CSS_SELECTOR, 'input[name=c_email]')
            locator_senha = (By.CSS_SELECTOR, 'input[name=senha]')
            locator_confirma_senha = (By.CSS_SELECTOR, 'input[name=c_senha]')
            locator_submit = (By.CSS_SELECTOR, 'input[name=button]')
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='nome'))  # quando existir "nome" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=nome]').send_keys('gabriel')  # ESCREVE NO INPUT NOME
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='email'))  # quando estiver "email" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=email]').send_keys('gabriel@live.com')  # ESCREVE NO INPUT email
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='c_email'))  # quando estiver "c_email" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=c_email]').send_keys('gabriel@live.com')  # ESCREVE NO INPUT c_email
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='senha'))  # quando estiver "senha" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=senha]').send_keys('blablabla')  # ESCREVE NO INPUT senha
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='c_senha'))  # quando estiver "c_senha" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=c_senha]').send_keys('blablabla')  # ESCREVE NO INPUT c_senha
            
            wdw.until(text_to_be_present_in_element(locator=(By.CSS_SELECTOR, 'body > div > div > h4'), text_='button'))  # quando estiver "button" no h4...
            self.chrome.find_element(By.CSS_SELECTOR, 'input[name=button]').click() # ESCREVE NO INPUT button
            
            
            
        try:
            executa()
        except Exception:
            self.chrome.refresh()
            executa()
            
        
qualquerver = input('qual vc quer ver, por text(1) ou por value(2): ')
chrome = FormSubmitGo()


if qualquerver == '1':
    chrome.ver_por_text()
elif qualquerver == '2':
    chrome.ver_por_value()