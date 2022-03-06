from functools import partial
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def espera_elemento(webelement, webdriver):
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
    print(f'Tentando encontrar {webelement}')
    if webdriver.find_elements(By.CSS_SELECTOR, webelement):
        return True  # return true and finished function
    return False
    


url = 'https://selenium.dunossauro.live/aula_09_a.html'
chrome = Chrome()

wdw = WebDriverWait(driver=chrome, timeout=10, poll_frequency=0.5)


# TODOS -> passo a passo
chrome.get(url)  # 1 ABRIR A PAGE

# 2 ESPERAR BOTÃO APARECER
esperar_button = partial(espera_elemento, 'button')
wdw.until(method=esperar_button, message='NAO ACHEI O ELEMENTO!')  

# 3 CLICAR NO BOTÃO
chrome.find_element(By.CSS_SELECTOR, 'button').click()

# 4 ESPERAR A DIV QUE TEM O ID finished APARECER
esperar_div_sucesso = partial(espera_elemento, '#finished')
wdw.until(method=esperar_div_sucesso, message='NAO ACHEI O ELEMENTO!')  

# RECUPERA A DIV DE SUCESSO
div_sucesso = chrome.find_element(By.CSS_SELECTOR, '#finished')
print('A div é "Carregamento concluído"? ', div_sucesso.text == 'Carregamento concluído')