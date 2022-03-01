import selenium # importa o selenium
from parsel import Selector
# pega o arquivo com o html
from pprint import pprint as print  # MUDEI O PRINT COMUM PELO PPRINT
import os
os.system('cls' if os.name == 'nt' else 'clear')
with open('/home/gabriel/Documentos/My Documents/Curso de Selenium In Python/Palestra XPATH/receita_pudim_de_leite_condensado_XPATH/index.html') as file:
    contend = file.read() # salva todo o conteudo para a variavel contend
    
response = Selector(text=contend)  # pega o conteudo e organiza para trabalhar e encontrar algo

# print(response.get())  # mostra todo o arquivo html
'''
mostra todo o arquivo
'''


# print(response.xpath('/'))  # mostra o caminho absoluto XPATH
'''
/ a partir do começo do arquivo
'''

# print(response.xpath('/html'))  # mostra o html via XPATH
'''
O /html retorna um seletor que seria a mesma coisa do find_element_by_tag_name()

/html a partir da raiz o elemento html que tiver a baixo, que seria o elemento todo
'''

# print(response.xpath('/html/head').get())  # mostra o conteúdo de todo o head via XPATH

'''
mostra todo o conteudo que o head tem dentro

da raiz / pega o html /html do html pega o head /html/head
'''

# print(response.xpath('/html/head/title').get())  # mostra o conteúdo de todo o title via XPATH

'''
e para pegar o title:
/html/head/title -> da raiz, pega o html, e do html, pega o head e do head pega o title
'''

# print(response.xpath('/title').get())  # retorna None

'''
Nao retorna nada pq da raiz nao tem um title, só um html
'''

'''E se eu quero pegar o titulo mas eu nao sei a arvore toda para encotrar.
ou a arvore do arquivo html é muito complicada para achar...

usa-se o //'''
# print(response.xpath('//title').getall())  # o // pega todas as tags title que tem nos documentos

'''usando o .getall() pega todos os elementos de um documento'''

# print(response.xpath('//h1').getall())  # pega todos os h1 do documento

'''mostrando todos os h1'''

# print(response.xpath('//ul').getall())  # pega todos os UL do documento

'''Pega todos os ul da página'''

# print(response.xpath('//ul/*').getall())  # pega todos os LI do documento dentro da hierarquia do UL

'''COM /* RETORNA QUALQUER TAG QUE VIER LOGO ABAIXO DO UL OU SEJA os li's
['<li><span class="qtde" data-qtde="1">1</span> <span>xícara de '
 'açúcar</span></li>',
 '<li><span class="qtde" data-qtde="1">1</span> <span>caixa de leite de '
 'condensado</span></li>',
 '<li><span class="qtde" data-qtde="2">2</span> <span>medidas de '
 'leite</span></li>',
 '<li><span class="qtde" data-qtde="3">3</span> <span>ovos</span></li>']

'''

# print(response.xpath('//ul//*').getall())  # pega todas as tags que estão abaixo do documento, inclusive as que estão fora da hierarquia do UL

'''COM //* pega todas as tags que estão abaixo do documento, inclusive as que estão dentro da hierarquia do primeiro elemento (aninhadas) do UL
estou pegando todos os filhos e nao só filho seguinte
['<li><span class="qtde" data-qtde="1">1</span> <span>xícara de '
 'açúcar</span></li>',
 '<span class="qtde" data-qtde="1">1</span>',
 '<span>xícara de açúcar</span>',
 '<li><span class="qtde" data-qtde="1">1</span> <span>caixa de leite de '
 'condensado</span></li>',
 '<span class="qtde" data-qtde="1">1</span>',
 '<span>caixa de leite de condensado</span>',
 '<li><span class="qtde" data-qtde="2">2</span> <span>medidas de '
 'leite</span></li>',
 '<span class="qtde" data-qtde="2">2</span>',
 '<span>medidas de leite</span>',
 '<li><span class="qtde" data-qtde="3">3</span> <span>ovos</span></li>',
 '<span class="qtde" data-qtde="3">3</span>',
 '<span>ovos</span>']
'''

'''SE QUISER SÓ O FILHO USA SÓ UMA BARRA /* O OS FILHOS DO FILHO //*'''

###########################

# print(response.xpath('//ol').getall())  # pega todas as tags ol que estão no documento que é a lista ordenada por números

'''cle['<ol>\n'
 '                <li>Em uma panela de fundo largo, derreta o açúcar até ficar '
 'dourado.</li>\n'
 '                <li>Junte meia xícara (chá) de água quente e mexa com uma '
 'colher.</li>\n'
 '                <li>Deixe ferver até dissolver os torrões de açúcar e a '
 'calda engrossar.</li>\n'
 '                <li>Forre com a calda uma forma com furo central (19 cm de '
 'diâmetro) e reserve.</li>\n'
 '            </ol>',
 '<ol>\n'
 '                <li>Em um liquidificador, bata todos os ingredientes do '
 'pudim e despeje na forma reservada.</li>\n'
 '                <li>Cubra com papel-alumínio e leve ao forno médio (180°C), '
 'em banho-maria, por cerca de 1 hora e 30 minutos.</li>\n'
 '                <li>Depois de frio, leve para gelar por cerca de 6 horas. '
 'Desenforme e sirva a seguir.</li>\n'
 '            </ol>']

'''

# print(response.xpath('//ol/li').getall()) # pega todos os li

'''
['<li>Em uma panela de fundo largo, derreta o açúcar até ficar dourado.</li>',
 '<li>Junte meia xícara (chá) de água quente e mexa com uma colher.</li>',
 '<li>Deixe ferver até dissolver os torrões de açúcar e a calda '
 'engrossar.</li>',
 '<li>Forre com a calda uma forma com furo central (19 cm de diâmetro) e '
 'reserve.</li>',
 '<li>Em um liquidificador, bata todos os ingredientes do pudim e despeje na '
 'forma reservada.</li>',
 '<li>Cubra com papel-alumínio e leve ao forno médio (180°C), em banho-maria, '
 'por cerca de 1 hora e 30 minutos.</li>',
 '<li>Depois de frio, leve para gelar por cerca de 6 horas. Desenforme e sirva '
 'a seguir.</li>']
 
'''


# print(response.xpath('//ol/li[2]').getall()) # ele pega o segundo li do primeiro ol e o segundo li do segundo ol

'''O xpath é indexado em 1 (e nao em 0 como uma lista python)
quando faz //ol/li[2] ele pega o segundo li do primeiro ol e o segundo li do segundo ol

'''

# print(response.xpath('(//ol/li)[2]').getall())  # pega o segundo li do primeiro ol que achar
# print(response.xpath('//ol[1]/li[2]').getall())  # pega de todos os ol o primeiro e de todos os li o segundo


'''
para pegar só o segundo li do primeiro ol que achar
print(response.xpath('(//ol/li)[2]').getall())  # pega o segundo li do primeiro ol que achar


 pega de todos os ol o primeiro e de todos os li o segundo
 print(response.xpath('//ol[1]/li[2]').getall())  # pega de todos os ol o primeiro e de todos os li o segundo

'''

'''
SEM O PARENTESES //ol/li estou pegando de todos os ol (pega os 2 ol) e de todos os 2 ol pega todos os li

COM O PARENTESES (//ol/li) estou pegando de todos os ol (pega os 2 ol) e de todos os 2 ol pega todos os li 
    MAS A PARTIR DO PARENTESES FINAL ) VAI ESTAR SE REFERINDO AO CONJUNTO DE LI. AS OPERACOES FEITAS A PARTIR
    DO ) VAI SER SÓ NOS LI'S
    
'''

'''

GERALMENTE QUANDO COPIA O XPATH DO NAVEGADOR, ELE RETORNA O CAMINHO ABSOLUTO : /html/body/div/div[3]/ol[1]/li[2]
SE A PAGINA FOR UMA OUTRA RECEITA QUE TIVER MAIS DE UMA LISTA. O CAMINHO ESTA TAO ATRELADO Ã UM RELACIONAMENTO DE ELEMENTOS
QUE PODE VARIAR

'''
#################################
'''
PARA ISSO É BOM OLHAR OS ATRIBUTOS POR EXEMPLO O h1 TEM O data-section="instructions"

'''
# print(response.xpath('//h1').getall())  # retorna todos os h1

# print(response.xpath('//h1//text()').getall())  # retorna o texto de todos os h1
'''
PARA RECUPERAR O TEXTO DO ELEMENTO(S) SELECIONADO(S) USA-SE text() no final do XPATH -> //h1/text()
nesse caso não veio o primeiro h1 porque usou uma / antes do text  -> //h1{/}text()
    assim ele só pega o texto que está logo abaixo do h1 e nao nada que estiver dentro de um filho dele
    
    para recuperar todos, tem que usar o //h1//text() que pega qualquer texto que esteja dentro de um filho
'''

# print(response.xpath('//ul[2]/li[3]/text()').getall()) # retorna um espaco vazio
'''retorna um espaco vazio porque do elemento li, tem um span e outro span e entre os spans tem um espaco
<li><span class="qtde" data-qtde="3">3</span> <span>ovos</span></li>
'''

# print(response.xpath('//ul[2]/li[3]//text()').getall()) # retorna todos os elementos que achar no li, tanto os que estao dentro dos spans quanto dos que estáo fora
'''retorna todos os elementos que achar no li, tanto os que estao dentro dos spans quanto dos que estáo fora
<li<span class="qtde" data-qtde="3">3</span> <span>ovos</span></li>
'''

# print(response.xpath('//ul[2]/li[3]/span/text()').getall()) # retorna todos os elementos estao dentro do span
'''retorna todos os elementos que achar no li, tanto os que estao dentro dos spans quanto dos que estáo fora
<li<span class="qtde" data-qtde="3">3</span> <span>ovos</span></li>
'''


# print(response.xpath('//h1/@data-section').getall()) # retorna o conteúdo do atributo dos elementos que escolheu ou seja o que tem dentro do nome do atributo
'''pegar os elementos pelo atributo (classe ou id)
    retorna o texto dos atributos
'''

# print(response.xpath('//a/@href').getall()) # retorna o conteúdo do atributo ou seja o que tem dentro do nome do atributo
'''pega os links de todas as ancoras

'''


# print(response.xpath('//h1[@data-section]').getall())  # pega os h1 que tem o atributo escolhido 
'''
pegar h1 que tenha o atributo escolhido
ESSE É BOM PARA QUANDO SE TEM tr E th (VEJA ABAIXO)
'''
# print(response.xpath('//tr[th]').getall())
'''pega todas as tr que tenham um th'''

# print(response.xpath("//li[contains(text(), 'forno')]").getall())
'''pega todas as li que contenham forno como texto'''

# print(response.xpath("//li/span[contains(text(), 'leite')]").getall())
'''pega todas as li e dos li pega os span que contenham leite como texto'''


# print(response.xpath("//li[contains(., 'leite')]").getall())
'''quando usamos o . eu estou me referindo ao próprio elemento, nenhum abaixo dele

EU QUERO TODOS OS LI E QUE DENTRO DO CONTEUDO DE CADA LI CONTENHA LEITE
'''

# print(response.xpath("//li[not(contains(text(), 'forno'))]").getall())
'''pegar todos os li que NAO contenha 'forno' no texto

    //li = todos os li da pagina
    
    [not(contains(text(), = nao contem o texto
    
    'forno'))] = forno na pagina
    
    
'''

# print(response.xpath('//tr[not(th)]').getall())
'''pegar todos os tr que NAO contenha th 
    
'''

# print(response.xpath('//h1[not(@data-section)]').getall())
'''retorna todos os h1 que NAO contenha o atributo data-section 
    
    //h1 = todos os h1
    [not(@data-section)] = que nao tenha o atributo data-section
'''

# print(response.xpath('//h1[not(@data-section)]').getall())
'''retorna todos os h1 que NAO contenha o atributo data-section 
    
    //h1 = todos os h1
    [not(@data-section)] = que nao tenha o atributo data-section
'''

# print(response.xpath('//span[@data-qtde!="2"]').getall())
'''retorna todos os span que tenham o atributo data-qtde diferente de '2'
    é possível utilizar igual (=) ou diferente (!=)
    //h1 = todos os h1
    [not(@data-section)] = que nao tenha o atributo data-section
'''

# print(response.xpath('//span[@data-qtde>"2"]').getall())
'''retorna todos os span que tenham o atributo data-qtde for maior que 2
formas possíveis: 
    print(response.xpath('//span[@data-qtde>2]').getall())  # sem aspas
    print(response.xpath('//span[@data-qtde>"2"]').getall())  # com aspas


    é possível utilizar igual (=) ou diferente (!=) maior que (>) menor que (<)
    //h1 = todos os h1
    [not(@data-section)] = que nao tenha o atributo data-section
'''
####################################### irmaos, parentes, ancestrais... ###################################

# print(response.xpath('//h1[@data-section="ingredients"]/parent::div//li').getall())  
# a partir do h1 que tem o atributo ingredients, recupere o parente que é a div anterior. e dessa div anterior, recupere todos os li
'''
recuperar li de ingredientes

os li de ingredientes estao dentro de uma div que tem um h1 que tem um atributo data-section que recebe ingredients

//h1[@data-section="ingredients"] -> self
# elemento que está sendo recuperado

//h1[@data-section="ingredients"]/parent::div -> parent
# parent div é a div anterior que o elemento atual (h1)

'''


# print(response.xpath('//h1[@data-section="ingredients"]/following-sibling::ul/li').getall())  
# a partir do h1 que tem o atributo ingredients, recupere os irmaos do h1 que seja os ul (recupera todos os ul que estão proximos de h1) e 
# desse ul, pega todos os li
'''
recuperar li de ingredientes

os li de ingredientes estao dentro de uma div que tem um h1 que tem um atributo data-section que recebe ingredients

//h1[@data-section="ingredients"] -> self
# elemento que está sendo recuperado

//h1[@data-section="ingredients"]/parent::div -> parent
# parent div é a div anterior que o elemento atual (h1)

'''

print(response.xpath('//h2[contains(text(), "Pudim") and contains(./preceding-sibling::h1/@data-section, "ingredients")]').getall())

'''
//h2 -> de todos os h2

[contains(text(), "Pudim")  --> que contem o texto Pudim

and contains(./preceding-sibling::h1/@data-section, "ingredients")] e contenha também um h1 que é irmao dele que contenha o data-section (atributo) ingredients
'''


print(response.xpath('//h2[contains(text(), "Pudim") and contains(./preceding-sibling::h1/@data-section, "ingredients")]/following-sibling::ul/li').getall())
'''
pega lis de ingrediente do pudim

//h2 -> de todos os h2

[contains(text(), "Pudim")  --> que contem o texto Pudim

and contains(./preceding-sibling::h1/@data-section, "ingredients")] e contenha também um h1 que é irmao dele que contenha o data-section (atributo) ingredients
'''