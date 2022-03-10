from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# abre o chrome
chrome = Chrome(executable_path=ChromeDriverManager().install())

wdw = WebDriverWait(chrome, 60)

# vai para o link
chrome.get('https://selenium.dunossauro.live/aula_11_d.html')

chrome.switch_to.frame('iframe')  # muda para um iframe

chrome.find_element_by_css_selector('#nome').send_keys('oi')
