from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def espera_button(webdriver):
    """
    Qualquer função que espera por um elemento DEVE receber um
    WebDriver e SEMPRE retornar boolean (TRUE OU FALSE)
    
    ### Parâmetros
    * webdriver -> O webdriver que vem do WebDriverWait.until() ou  WebDriverWait.until_not()

        EX: wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)
            wdw.until(method=espera_elemento, message='Element(s) not found | Elemento(s) não encontrado')
    
    #### elementos que darão False:
    * bool([]) -> não existe nenhum elemento na lista
    * bool('') -> o elemento retornado não foi encontrado ou não existe
    * bool(()) -> tupla vazia
    * bool(0) -> 0 (zero)
    #### elementos que darão True:
    * bool(['1']) or bool(['']) or bool([[]]) or qualquer coisa dentro de uma lista
    * bool('1') or qualquer coisa dentro de uma string
    * bool((1)) or qualquer coisa dentro de um set
    * bool(1) or qualquer número
    
    """
    elemento = webdriver.find_elements(By.CSS_SELECTOR, 'button')
    print(f'Tentando encontrar {elemento}')
    return bool(elemento)

def espera_elemento(webdriver):
    """
    Qualquer função que espera por um elemento DEVE receber um
    WebDriver e SEMPRE retornar boolean (TRUE OU FALSE)
    
    ### Parâmetros
    * webdriver -> O webdriver que vem do WebDriverWait.until() ou  WebDriverWait.until_not()

        EX: wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)
            wdw.until(method=espera_elemento, message='Element(s) not found | Elemento(s) não encontrado')
    
    #### elementos que darão False:
    * bool([]) -> não existe nenhum elemento na lista
    * bool('') -> o elemento retornado não foi encontrado ou não existe
    * bool(()) -> tupla vazia
    * bool(0) -> 0 (zero)
    #### elementos que darão True:
    * bool(['1']) or bool(['']) or bool([[]]) or qualquer coisa dentro de uma lista
    * bool('1') or qualquer coisa dentro de uma string
    * bool((1)) or qualquer coisa dentro de um set
    * bool(1) or qualquer número
    
    """
    elemento = webdriver.find_elements(By.CSS_SELECTOR, '#finished')
    print(f'Tentando encontrar {elemento}')
    return bool(elemento)

url = 'https://selenium.dunossauro.live/aula_09_a.html'
chrome = Chrome()

wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)


# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

wdw.until(method=espera_button, message='NAO ACHEI O ELEMENTO!')  # 2 ESPERAR BOTÃO APARECER
chrome.find_element(By.CSS_SELECTOR, 'button').click()  # 3 CLICAR NO BOTÃO
wdw.until(method=espera_elemento, message='NAO ACHEI O ELEMENTO!')  # 4 ESPERAR PELA DIV QUE FALA QUE FOI FINALIZADO
sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')  # 5 PEGA O SUCESSO
assert sucesso.text == 'Carregamento concluído'