from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_06_a.html'
chrome.get(url)

# pega brs irmaos de divs em form-group
chrome.find_elements_by_css_selector('div.form-group + br') 
# da primeira div qe tem a classe form-group pega todos os brs que estao no mesmo nível de hierarquia

# baseado na primeira div que tem a classe form-group pega o br que será filho dessa div
chrome.find_element_by_css_selector('div.form-group > br')

# do form pega os filhos que sejam div's
chrome.find_elements_by_css_selector('form > div')

# achar todos os br que estáo dentro do form
chrome.find_elements_by_css_selector('form br')

# do h2, pegue todos os br que estão na mesma posição
chrome.find_elements_by_css_selector('h2 ~ br')

# https://flukeout.github.io