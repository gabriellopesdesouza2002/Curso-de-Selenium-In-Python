from selenium.webdriver import Chrome
from time import sleep
browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser.get(url)
sleep(3)
a = browser.find_element_by_tag_name('a')

for vezes in range(10):
    a.click()
else:
    p = browser.find_elements_by_tag_name('p')  # é uma lista

print(f'O texto de a: {a.text}')
count = 0
for num in p:
    print(f'O texto de cada p é: {num.text}. (click atual: {count})')
    count += 1
sleep(3)
browser.quit()