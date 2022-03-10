from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_c.html')

wdw = WebDriverWait(driver=chrome, timeout=30)

print(f'qtd de janelas até agora {len(chrome.window_handles)}')

for i in range(10):
    wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button')))
    chrome.find_element(By.CSS_SELECTOR, 'button').click()
    print(f'qtd de janelas até agora {len(chrome.window_handles)}')
