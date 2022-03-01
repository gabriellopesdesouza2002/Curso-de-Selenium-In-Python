def open_chrome(url='https://www.python.org/doc/', time_for_sleep=3):
    """
    Para abrir o chrome sem o webdriver-manager utilize o chromedriver.
    
    ##### PARÂMETROS
    url = envie a sua url
    
    time_for_sleep = escolha o tempo de espera para fechar o navegador
    
    #### time_for_sleep tem por padrão fechar o navegador após 3 segundos
    #### A url utilizada por padrão é: https://www.python.org/doc/
    """
    
    from selenium.webdriver import Chrome
    from time import sleep
    
    chrome = Chrome()
    chrome.get(url)
    sleep(time_for_sleep)
    return
