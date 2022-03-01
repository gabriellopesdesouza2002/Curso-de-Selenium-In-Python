import os
os.system('cls' if os.name == 'nt' else 'clear')

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

chrome = Chrome()
url = 'https://selenium.dunossauro.live/exercicio_06.html'
chrome.get(url)
sleep(1)

form_l0c0 = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c0] div[class="form-group form-btn"] > input[name="l0c0"]').get_attribute('name')


form_l0c1 = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c1] div[class="form-group form-btn"] > input[name="l0c1"]').get_attribute('name')


form_l1c0 = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c0] div[class="form-group form-btn"] > input[name="l1c0"]').get_attribute('name')


form_l1c1 = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c1] div[class="form-group form-btn"] > input[name="l1c1"]').get_attribute('name')


for inutil in range(6):
    sleep(1)
    
    # pelo seletor do css, pegue a div que tem o id grid e dentro dele pegue um span que é filho do p que é filho do header
    form_indicado_a_preencher = chrome.find_element(By.CSS_SELECTOR, 'div#grid header > p > span').text
    
    if form_indicado_a_preencher == form_l0c0:
        # nome
        nome = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c0]  div:nth-child(2) > input[name="nome"]')
        # da div que tem o id=grid pegue o formulario que tem a classe=form-l0c0 a partir daqui, pegue a div que está na 2 posiçao como filha do form e dentro dessa div, pegue o input que tem o name=nome 
        
        senha = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c0]  div:nth-child(4) > input[name="senha"]')
        #div que tem id=grid pegue o form que tem a classe=form-l0c0 a partir daqui, pegue a div que é a quarta filha do form e dentro dessa div, recupere o input que tem o atributo nome=senha
        
        
        submit = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c0] div[class="form-group form-btn"] > input[name="l0c0"]')
        # da div que tem o id=Grid recupere o form que tem a classe=form-l0c0 a partir daqui, pegue a UNICA div que tem a classe form-group form-btn e recupere a filha que é um input do atributon name=l0c0
        
        
        nome.send_keys(f'{randint(1, 999999)}')
        senha.send_keys(f'{randint(1, 999999)}')
        submit.click()
        
    if form_indicado_a_preencher == form_l0c1:
        # nome
        nome = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c1]  div:nth-child(2) > input[name="nome"]')
        # da div que tem o id=grid pegue o formulario que tem a classe=form-l0c1 a partir daqui, pegue a div que está na 2 posiçao como filha do form e dentro dessa div, pegue o input que tem o name=nome 
        
        senha = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c1]  div:nth-child(4) > input[name="senha"]')
        #div que tem id=grid pegue o form que tem a classe=form-l1c1 a partir daqui, pegue a div que é a quarta filha do form e dentro dessa div, recupere o input que tem o atributo nome=senha
        
        
        submit = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l0c1] div[class="form-group form-btn"] > input[name="l0c1"]')
        # da div que tem o id=Grid recupere o form que tem a classe=form-l1c1 a partir daqui, pegue a UNICA div que tem a classe form-group form-btn e recupere a filha que é um input do atributon name=l1c1
        
        
        nome.send_keys(f'{randint(1, 999999)}')
        senha.send_keys(f'{randint(1, 999999)}')
        submit.click()
        
    if form_indicado_a_preencher == form_l1c0:
        # nome
        nome = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c0]  div:nth-child(2) > input[name="nome"]')
        # da div que tem o id=grid pegue o formulario que tem a classe=form-l1c1 a partir daqui, pegue a div que está na 2 posiçao como filha do form e dentro dessa div, pegue o input que tem o name=nome 
        
        senha = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c0]  div:nth-child(4) > input[name="senha"]')
        #div que tem id=grid pegue o form que tem a classe=form-l1c1 a partir daqui, pegue a div que é a quarta filha do form e dentro dessa div, recupere o input que tem o atributo nome=senha
        
        
        submit = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c0] div[class="form-group form-btn"] > input[name="l1c0"]')
        # da div que tem o id=Grid recupere o form que tem a classe=form-l1c1 a partir daqui, pegue a UNICA div que tem a classe form-group form-btn e recupere a filha que é um input do atributon name=l1c1
        
        
        nome.send_keys(f'{randint(1, 999999)}')
        senha.send_keys(f'{randint(1, 999999)}')
        submit.click()
        
    if form_indicado_a_preencher == form_l1c1:
        # nome
        nome = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c1]  div:nth-child(2) > input[name="nome"]')
        # da div que tem o id=grid pegue o formulario que tem a classe=form-l1c1 a partir daqui, pegue a div que está na 2 posiçao como filha do form e dentro dessa div, pegue o input que tem o name=nome 
        
        senha = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c1]  div:nth-child(4) > input[name="senha"]')
        #div que tem id=grid pegue o form que tem a classe=form-l1c1 a partir daqui, pegue a div que é a quarta filha do form e dentro dessa div, recupere o input que tem o atributo nome=senha
        
        
        submit = chrome.find_element(By.CSS_SELECTOR, 'div#grid form[class=form-l1c1] div[class="form-group form-btn"] > input[name="l1c1"]')
        # da div que tem o id=Grid recupere o form que tem a classe=form-l1c1 a partir daqui, pegue a UNICA div que tem a classe form-group form-btn e recupere a filha que é um input do atributon name=l1c1
        
        
        nome.send_keys(f'{randint(1, 999999)}')
        senha.send_keys(f'{randint(1, 999999)}')
        submit.click()