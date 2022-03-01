from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
driver = Firefox()
driver.get(url)
sleep(4)
list_ps = driver.find_elements_by_tag_name('p')

# achando o p que tem o número esperado:
p_com_o_n_esperado = ''
for p in list_ps:
    if 'esperado:' in p.text:
        p_com_o_n_esperado = p.text
    else:
        ...
numero_esperado_for_parsing = p_com_o_n_esperado[-2:].split()
numero_esperado = ''
for n in numero_esperado_for_parsing:
    numero_esperado = n

print(p_com_o_n_esperado)
print(numero_esperado)


def clica_p_achar():
    lista_ps_text = []
    list_ps = driver.find_elements_by_tag_name('p')
    for item in list_ps:
        lista_ps_text.append(item.text)
    print(lista_ps_text)
    sleep(1)
    clica = driver.find_element_by_tag_name('a').click()
    while 'ganhou' not in lista_ps_text[-1]:
        clica_p_achar()
    else:
        exit()
clica_p_achar()


sleep(1)
driver.quit()
