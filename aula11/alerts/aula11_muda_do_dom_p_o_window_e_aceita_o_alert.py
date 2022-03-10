from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_a.html')

wdw = WebDriverWait(driver=chrome, timeout=30)
wdw.until(EC.element_to_be_clickable(locator=(By.CSS_SELECTOR, '#alert')))
id = chrome.find_element(By.CSS_SELECTOR, '#alert')
id.click()

# muda para o alerta
alerta = chrome.switch_to.alert

# # dir(alerta) -> ver o que o alerta pode fazer
# dir(alerta)

# # pegando o texto do alerta | 'Isso é um alerta'
# alerta.text

# aceita o alerta e voltamos para o DOM
alerta.accept()