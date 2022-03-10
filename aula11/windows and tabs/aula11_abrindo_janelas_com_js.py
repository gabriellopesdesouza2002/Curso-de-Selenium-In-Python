from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# abre o chrome
chrome = Chrome(executable_path=ChromeDriverManager().install())

# vai para o link
chrome.get('https://selenium.dunossauro.live/aula_11_c.html')


def abre_aba_e_pesquisa_por_url(url='https://ddg.gg'):
    """
    ### Essa função abre uma nova janela com a url que vc desejar
    """
    
    # abre uma aba em branco
    chrome.execute_script('window.open()')
    
    # pega todas as janelas
    windows = chrome.window_handles

    # muda para a ultima janela
    chrome.switch_to.window(windows[-1])

    # envia o seu link para essa nova janela
    chrome.get(url)

abre_aba_e_pesquisa_por_url('https://google.com.br')