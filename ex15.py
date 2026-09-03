# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa
# declarar
a: float = 0
b: float = 0
h: int = 0
# inicio
# recebe o valor de a
a = float(input('Digite o valor de A: '))

# recebe o valor de b
b = float(input('Digite o valor de B: '))

# calcula a hipotenusa
h = (a**2 + b**2) ** 0.5

# retona a hipotenusa
print('O valor da hipotenusa é:', int(h))
