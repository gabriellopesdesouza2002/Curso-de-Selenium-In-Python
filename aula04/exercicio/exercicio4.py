'''
1 pegar todos os links das aulas
    {'nome da aula': 'link da aula' }
2 navegar até o exercicio 3
    achar a url do ex 3 e ira até la
'''

from email.quoprimime import body_check
from importlib.resources import path
from time import sleep
from turtle import title
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


def click_first_link(driver, elemento_principal=''):
    '''
    ## Clica no primeiro link que eu achar
    
        Você manda um elemento_principal (ex: 'body')
        e eu clicarei no primeiro link que eu achar
        no elemento_principal (ex: 'body')
        
        - driver = Instância do navegador
        - elemento_principal = webelement [aside, main, body, ul, ol]
        return -> dict com os links e os seus text's
        
    '''
    elemento_principal = driver.find_element(By.TAG_NAME, elemento_principal)
    elemento_principal.find_element(By.TAG_NAME, 'a').click()
        
        
        
def get_first_text(driver, elemento_principal=''):
    '''
    ## Recupera o texto do primeiro elemento que eu achar
    
        Você manda um elemento_principal (ex: 'body')
        e eu pegarei o primeiro texto que eu achar
        no elemento_principal (ex: 'body')
        
        - driver = Instância do navegador
        - elemento_principal = webelement [aside, main, body, ul, ol]
                (pega os textos de todo o elemento)
        - elemento_principal = webelement [h1, a, p, li, ...]
                (pega o texto do elemento)
        
    '''
    elemento_principal = driver.find_elements(By.TAG_NAME, elemento_principal)
    for i in elemento_principal:
        return i.text
        break
    

def get_second_text(driver, elemento_principal='', posicao_do_item=0):
    '''
    ## Recupera o texto do segundo elemento que eu achar
    
        Você manda um elemento_principal (ex: 'body')
        e eu pegarei o segundo texto que eu achar
        no elemento_principal (ex: 'body')
        
        
        - driver = Instância do navegador
        - elemento_principal = webelement [aside, main, body, ul, ol]
                (pega os textos de todo o elemento)
        - elemento_principal = webelement [h1, a, p, li, ...]
                (pega o texto do elemento)
        
    '''
    elemento_principal = driver.find_elements(By.TAG_NAME, elemento_principal)
    elemento_text = elemento_principal[posicao_do_item]
    return elemento_text.text
        
def convert_calcula_str_nums(strig_format):
    '''
    # Formatos válidos : (4 * 7 =, 4 * 10 =, 10 * 10 =)
    
    ### retorna a multiplicacao dos valores
    
        * string_format = ['4 * 7 =', '4 * 10 =', '33 * 33 =']
        * len(string_format) = 7, 8, 9
    '''
    
    calcular_format = strig_format[:-1]  # remove o sinal de igual (=)
    primeiro_numero = calcular_format[0:2].strip()  # pega o primeiro número e remove os eventuais espacos
    segundo_numero = calcular_format[-3:].strip()  # pega o segundo número e remove os eventuais espacos
    primeiro_numero = int(primeiro_numero)  # converte o primeiro número p/ int
    segundo_numero = int(segundo_numero)  # converte o segundo número número p/ int
    return (primeiro_numero  * segundo_numero)  # retorna o a multiplicação do primeiro com o segundo número
    
    
def get_texts_in_links(driver, elemento_principal=''):
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
    texts = []
    elemento_principal = driver.find_element(By.TAG_NAME, elemento_principal)
    links = elemento_principal.find_elements(By.TAG_NAME, 'a')
    for link in links:
        texts.append(link.text)
    
    return texts

exercicios = get_links(chrome, 'main')  # procura pelos links
pprint(exercicios)  # mostra os e os exercicios links
chrome.get(exercicios['Exercício 3'])  # vai para o link onde a chave é Exercício 3
click_first_link(chrome, 'main')  # vai para o primeiro link que a funcao achar
sleep(.5)
pega_primeiro_texto = get_first_text(chrome, 'h1')
print(pega_primeiro_texto)
calcular = get_second_text(chrome, 'p', 1)
calculado = convert_calcula_str_nums(calcular)
texto = get_texts_in_links(chrome, 'main')
sleep(2)
for i in texto:
    i = int(i)
    if i == calculado:
        print('igual')
    else:
        sleep(2)
        chrome.find_element_by_xpath(f'//*[@id="main"]/li//a[@attr="errado"]').click()
        sleep(3)
        break
chrome.refresh()
chrome.refresh()
chrome.refresh()
sleep(21)
titulo = chrome.title
print(titulo)
titles = get_texts_in_links(chrome, 'main')
sleep(2)
for titulo_f in titles:
    if titulo_f == titulo:
        chrome.find_element_by_xpath(f'//*[@id="main"]/li//a[@attr="certo"]').click()

sleep(5)

path_url = urlparse(chrome.current_url).path
path_tratada = path_url[1:]
print(path_tratada)

paths = get_texts_in_links(chrome, 'main')
for path_do_path in paths:
    if path_do_path == path_tratada:
        chrome.find_element_by_xpath(f'//*[@id="main"]/li//a[@href="page_4.html"]').click()

