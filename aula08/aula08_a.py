from xml.dom.minidom import Element
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pyautogui

from random import randint
chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_08_a.html'
texto = "selenium"

chrome.get(url)

# Hi-level
input = chrome.find_element(By.CSS_SELECTOR, 'textarea')  # esse sempre tem que recuperar com hi-level
# input.send_keys(texto)

# # Low-Level (clicando só na primeira letra)
# ac = ActionChains(chrome)
# ac.key_down(texto[0])
# ac.key_up(texto[0])
# ac.perform()

# Low-Level (clicando só na primeira letra COM SHIFT)

ac = ActionChains(chrome)
ac.move_to_element(input)  # foca no elemento textarea para clicar
ac.click(input)  # clica no elemento para pegar o foco
def digita_com(key):
    ac.key_down(key)  # pressiona o shift
    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)
    ac.key_up(key)  # solta o shift

# digita_com(Keys.SHIFT)
digita_com(Keys.SHIFT)

ac.perform()