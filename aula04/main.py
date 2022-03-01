'''
1 pegar todos os links das aulas
    {'nome da aula': 'link da aula' }
2 navegar até o exercicio 3
    achar a url do ex 3 e ira até la
'''

from email.quoprimime import body_check
from time import sleep
from unittest import result
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from pprint import pprint
import os

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_04.html')
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

'''
PARTE 1
'''

def get_links(driver, elemento_principal=''):
    '''
    Pega todos os links de dentro de um elemento:
    
        Você manda um elemento_principal (ex: 'body')
        e eu retornarei um dict com 
        todos os links que encontrar
        no elemento_principal (ex: 'body')
        
        - driver = Instância do navegador
        - elemento_principal = webelement [aside, main, body, ul, ol]
        return -> dict com os links e os seus text's
        
    '''
    link_dict = {}
    elemento_principal = driver.find_element(By.TAG_NAME, elemento_principal)
    links = elemento_principal.find_elements(By.TAG_NAME, 'a')
    for link in links:
        link_dict[link.text] = link.get_attribute('href')
        # dict      chave    :      valor
    
    return link_dict
    
aulas = get_links(chrome, 'aside')
exercicios = get_links(chrome, 'main')

pprint(aulas)
pprint(exercicios)
