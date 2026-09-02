# Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.
# declarar
n1: int = 0
n2: int = 0
soma: int = 0
# inicio
# recebe o valor do primeiro numero
n1 = int(input('Digite um número: '))

# recebe o valor do segundo numero
n2 = int(input('Digite um segundo número: '))

# Faz n1 e n2 ao quadrado
n1 = n1**2
n2 = n2**2

# soma n1 e n2
soma = n1+n2

# retona a soma
print('\nO valor de n1 ao quadrado mais n2 ao quadrado é:', soma)
