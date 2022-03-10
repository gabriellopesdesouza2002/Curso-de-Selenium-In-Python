from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_b.html')

def find_window_to_title(title_switch: str): # quero um titulo que seja str
    """
    ### Essa função muda de janela quando o título for igual ao parametro enviado
    #### Ex -> Minha janela  = Minha janela
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = chrome.window_handles # ids de todas as janelas

    for window in window_ids:
        chrome.switch_to_window(window)  
        if chrome.title == title_switch:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {title_switch}')
        
def find_window_to_title_contain(title_contain_switch: str): # quero que pelo menos um pedaco do titulo que seja str
    """
    ### Essa função muda de janela quando o título tiver pelo menos algo igual ao parametro enviado
    #### Ex -> Minha janela = janela
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for ao menos de um pedaço do titulo que passei
        em title_contain_switch
    para de executar
    """
    window_ids = chrome.window_handles # ids de todas as janelas

    for window in window_ids:
        chrome.switch_to_window(window)  
        if title_contain_switch in chrome.title:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {title_contain_switch}')
        
def find_window_to_url(url_switch: str): # quero uma url que seja str
    """
    ### Essa função muda de janela quando a url for igual ao parametro enviado
    #### Ex -> https://google.com.br  = https://google.com.br
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = chrome.window_handles # ids de todas as janelas

    for window in window_ids:
        chrome.switch_to_window(window)
        if chrome.current_url == url_switch:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {url_switch}')
          
def find_window_to_url_contain(contain_url_switch: str): # quero uma url que seja str
    """
    ### Essa função muda de janela quando a url conter no parametro enviado
    #### Ex -> https://google.com.br  = google
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = chrome.window_handles # ids de todas as janelas

    for window in window_ids:
        chrome.switch_to_window(window)
        if contain_url_switch in chrome.current_url:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {contain_url_switch}')
        
