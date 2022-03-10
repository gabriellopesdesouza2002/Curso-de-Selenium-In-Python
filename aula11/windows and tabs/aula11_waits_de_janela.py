from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# abre o chrome
chrome = Chrome(executable_path=ChromeDriverManager().install())

wdw = WebDriverWait(chrome, 60)

# vai para o link
chrome.get('https://selenium.dunossauro.live/aula_11_b.html')

chrome.find_element(By.CSS_SELECTOR, '#popupd')


# # verifica se abriu alguma janela
# wdw.until(EC.new_window_is_opened(chrome.window_handles))
# print('Janela aberta')


# # verifica se abriu x numeros de janelas
# wdw.until(EC.number_of_windows_to_be(2))
# print(f'tem {len(chrome.window_handles)} janelas')