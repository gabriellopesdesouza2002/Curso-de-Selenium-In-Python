calcular = '4 * 5 ='

print(len(calcular))
calcular_format = calcular[:-1]
primeiro_numero = calcular_format[0:2].strip()
segundo_numero = calcular_format[-3:].strip()
primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)


print(calcular_format)
print(primeiro_numero)
print(segundo_numero)
print(primeiro_numero * segundo_numero)