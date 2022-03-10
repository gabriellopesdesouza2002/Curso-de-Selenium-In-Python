from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_b.html')

wdw = WebDriverWait(driver=chrome, timeout=30)

chrome.current_window_handle # id da janela atual

sleep(20)
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#popup')))
chrome.find_element(By.CSS_SELECTOR, '#popup').click()
print(chrome.current_url)
        
def find_window_to_url(url_switch: str):
    window_ids = chrome.window_handles

    for window in window_ids:
        chrome.switch_to_window(window)
        if chrome.current_url == url_switch:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {url_switch}')

find_window_to_url('https://selenium.dunossauro.live/popup.html')
print(chrome.current_url)
