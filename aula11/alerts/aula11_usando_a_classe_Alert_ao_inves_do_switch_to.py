from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ALERT
from selenium.webdriver.common.alert import Alert

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://selenium.dunossauro.live/aula_11_a.html')

wdw = WebDriverWait(driver=chrome, timeout=30)
wdw.until(EC.element_to_be_clickable(locator=(By.CSS_SELECTOR, '#alert')))
id = chrome.find_element(By.CSS_SELECTOR, '#alert')
id.click()


# passamos ou o browser ou o elemento
alerta = Alert(chrome)  # ele retorna um alert
# ao invés de dar o switch to damos um a gente vai abrir o alerta de cara
# aqui ele vai lidar com erros

# aceita o alerta e voltamos para o DOM
alerta.accept()