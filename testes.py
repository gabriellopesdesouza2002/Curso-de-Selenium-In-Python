from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome = Chrome(executable_path=ChromeDriverManager().install())
chrome.get('https://mail.google.com/mail/')

wdw = WebDriverWait(chrome, 20)

wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#identifierId')))
chrome.find_element(By.CSS_SELECTOR, '#identifierId').send_keys('meuemail@gmail.com')