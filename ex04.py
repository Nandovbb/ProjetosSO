# declarar
c: float = 0
f: float = 0
# inicio
# recebe o valor de celcius
c = float(input('Digite quantos graus em Celsius: '))

# calcula Fahrenheit usando o celcius
f = (9*c+160)/5

# retorna celcius e fahrenheit
print(c, 'Graus em celsius são:', f, 'em Fahrenheit.')
