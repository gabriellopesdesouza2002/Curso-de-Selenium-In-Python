from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located  # verifica se o elemento está na tela
)

url = 'https://selenium.dunossauro.live/aula_10_a.html'
chrome = Chrome()

chrome.get(url)

locator = (By.CSS_SELECTOR, '#request')

wdw = WebDriverWait(driver=chrome, timeout=30)  # vai esperar 30 seg caso de erro, ele vai ficar procurando pelo element

# wdw.until_not(
#     presence_of_element_located(locator)
#     )  # esperar que o elemento não esteja na tela para continuar o code
wdw.until(
    presence_of_element_located(locator)
    )  # esperar que o elemento esteja na tela para continuar o code

# clica no btn
chrome.find_element(*locator).click() #  *locator desempacota a tupla para a função 

