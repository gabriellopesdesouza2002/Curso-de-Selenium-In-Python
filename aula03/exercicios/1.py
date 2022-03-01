from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Chrome()
browser.get(url)
sleep(4)

titulo = browser.find_element_by_tag_name('h1')  # pega o titulo (no text)
dicio = {titulo.text: 'Vazio'}  # cria um dict com o titulo
dicio2 = {}  # cria um dicionario vazio para os ps

# para cada número no tamanho da lista que vem dos elementos
for n in range(0, len(browser.find_elements_by_tag_name('p'))):
    paragrafo = browser.find_elements_by_tag_name('p')  # o paragrafo é uma lista de todos as tags p
    dicio2.update({f'texto{n + 1}': paragrafo[n].text})
    '''O dici2 que é um dicionario vazio, recebe os valores de forma incrementada. a chave como texto{numero do range mais 1
    pois o range inicial é 0}
    e o valor paragrafo[posicao do item na lista recuperada pelo range].text que converte em texto'''

dicio = {titulo.text: dicio2}  # o dicionario principal recebe o titulo e agora o dicio2
print(dicio)

browser.quit()