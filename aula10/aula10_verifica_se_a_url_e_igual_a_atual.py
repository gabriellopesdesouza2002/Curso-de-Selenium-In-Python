from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    url_to_be,
)
"""
como o visibility_of_all_elements_located funciona

depois de todo l tem que ter um a,
ele vai esperar que todos os elementos sejam um a

"""
url = 'https://selenium.dunossauro.live/aula_10_c.html'
chrome = Chrome()

chrome.get(url)
wdw = WebDriverWait(driver=chrome, timeout=60)

link = chrome.find_element(By.CSS_SELECTOR, 'body > div > div > ul > li:nth-child(1) > a')
link.click()

# quero passar a URL QUE EU QUEIRA QUE ELE ESTEJA
wdw.until(url_to_be(url=url + '#'))

 
print(f'essa é a url inicial -> {url}#')
print(f'essa é a url atual -> {chrome.current_url}')
"""
quando clicamos no link -> mesma pagina
https://selenium.dunossauro.live/aula_10_c.html -> url atual
https://selenium.dunossauro.live/aula_10_c.html# -> url do link (mesma pagina)

"""