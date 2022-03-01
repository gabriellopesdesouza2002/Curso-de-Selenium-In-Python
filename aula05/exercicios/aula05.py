from time import sleep
from selenium.webdriver import Chrome

chrome = Chrome()

chrome.get('https://selenium.dunossauro.live/aula_05.html')
sleep(1)


# names= nome, email, senha, telefone, btn

# envia nome
chrome.find_element_by_xpath('//*[@id="nome"]').send_keys('Gabriel')
sleep(.5)
# Envia email
chrome.find_element_by_xpath('//*[@id="email"]').send_keys('gloryland@gmail.com')
sleep(.5)
# envia senha
chrome.find_element_by_xpath('//*[@id="senha"]').send_keys('itstrue')
sleep(.5)
# envia telefone
chrome.find_element_by_xpath('//*[@id="telefone"]').send_keys('(10)987654321')
sleep(.5)
# clica no enviar
chrome.find_element_by_xpath('//*[@name="btn"]').click()