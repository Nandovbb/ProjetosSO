# Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
# declarar
altura: int = 0
base: int = 0
area: int = 0
# inicio
# recebe a altura do triangulo
altura = int(input('Digite a altura do triangulo:'))

# recebe a base do triangulo
base = int(input('Digite a base do triangulo: '))

# faz o calculo da area do triangulo
area = altura * base / 2

# retorna a area do triangulo
print('A área do triangulo é: ', area)
