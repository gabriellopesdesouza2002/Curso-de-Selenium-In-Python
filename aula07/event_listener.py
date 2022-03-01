from selenium.webdriver import Chrome
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver  # pega o suporte (apoio) para eventos
from time import sleep
from random import randint

class Escuta(AbstractEventListener):  # a classe traz as caracteristicas do AbstractEventListener
    def before_click(self, element, driver):
        if element.tag_name == 'input':
            print(driver.find_element_by_css_selector('span').text)  # pegando o texto antes de clicar
            print(f'antes de clicar no {element.tag_name}')
        
    # def click(self, element, driver) -> None:
    #     print('clickando')  # isso nao funciona pq a ideia do ouvinte (escuta) é capturar o que veio ante o que vem dps
               
    def after_click(self, element, driver):
        if element.tag_name == 'input':
            print(driver.find_element_by_css_selector('span').text)  # pegando o texto antes de clicar
            print(f'antes de clicar no {element.tag_name}')

chrome = Chrome()

rap10 = EventFiringWebDriver(chrome, Escuta())

url = 'https://curso-python-selenium.netlify.app/aula_07_d.html'
rap10.get(url)

input_de_texto = rap10.find_element_by_css_selector('input')
span = rap10.find_element_by_css_selector('span')
p = rap10.find_element_by_css_selector('p')

print('To clicando...')
input_de_texto = rap10.find_element_by_css_selector('input').click()