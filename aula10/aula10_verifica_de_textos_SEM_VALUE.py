from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element,
)

url = 'https://selenium.dunossauro.live/aula_10_d.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

"""Saber se o elemento (pedaço de texto) está presente no elemento"""


"""LOCATORS"""
locator_h4 = (By.TAG_NAME, 'h4')
locator_nome = (By.CSS_SELECTOR, 'input[name=nome]')



# quero esperar que o texto esteja presente desse elemento
# o texto do h4 tem que estar presente no text_to_be
wdw.until(text_to_be_present_in_element(locator=locator_h4, 
                                        text_='Digite'))  # quando estiver "digite" no h4...
chrome.find_element(*locator_nome).send_keys('gabriel')  # ESCREVE NO INPUT NOME
