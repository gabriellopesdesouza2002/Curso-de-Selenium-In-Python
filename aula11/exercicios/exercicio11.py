"""
https://selenium.dunossauro.live/exercicio_12.html

preencher o form por meio dos prompts
depois que enviar, pegar o popup e validar as infos dele com as suas
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

# abre o firefox
firefox = Firefox(executable_path=GeckoDriverManager().install())
# firefox = Firefox(executable_path=GeckoDriverManager().install())

wdw = WebDriverWait(firefox, 60)

nome = "Gabriel"
email = 'gabriel@gmail.com'
signo = 'nao tenho'

# vai para o link
firefox.get('https://selenium.dunossauro.live/exercicio_12.html')

# espera o item estar disponível quando disponível JA ENTRA NELE
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=nome]')))
# clica no nome
firefox.find_element(By.CSS_SELECTOR, 'input[name=nome]').click()

# espera pelo alerta e da um switch para ele automaticamente
alerta = wdw.until(EC.alert_is_present())
alerta.send_keys(nome)  # envia para o alerta o nome
alerta.accept()  # aceita o alerta


# espera o item estar disponível 
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=email]')))
# clica no nome
firefox.find_element(By.CSS_SELECTOR, 'input[name=email]').click()

# espera pelo alerta e da um switch para ele automaticamente
alerta = wdw.until(EC.alert_is_present())
alerta.send_keys(email)  # envia para o alerta o nome
alerta.accept()  # aceita o alerta


# espera o item estar disponível 
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=signo]')))
# clica no nome
firefox.find_element(By.CSS_SELECTOR, 'input[name=signo]').click()

# espera pelo alerta e da um switch para ele automaticamente
alerta = wdw.until(EC.alert_is_present())
alerta.send_keys(signo)  # envia para o alerta o nome
alerta.accept()  # aceita o alerta

# espera o item estar disponível 
wdw.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value=Enviar]')))
# clica no nome
firefox.find_element(By.CSS_SELECTOR, 'input[value=Enviar]').click()


print(f'Você está na janela -> {firefox.current_window_handle}')

# verifica se abriu x numeros de janelas
wdw.until(EC.number_of_windows_to_be(2))
print(f'tem {len(firefox.window_handles)} janelas')
wids = firefox.window_handles

firefox.switch_to.window(wids[-1])
print(f'Você está na janela -> {firefox.current_window_handle}')

h1s = firefox.find_elements(By.CSS_SELECTOR, 'h1')
print('')

for h1 in h1s:
    print(h1.text)


