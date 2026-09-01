# declarar
import math
a: int = 0
b: int = 0
c: int = 0
d: int = 0
delta: int = 0
x1: int = 0
x2: int = 0
# inicio
# recebe o valor de A
a = int(input('Digite o valor de A: '))

# recebe o valor de b
b = int(input('Digite o valor de B: '))

# recebe o valor de c
c = int(input('Digite o valor de C: '))

# resolve a formula de delta
delta = (b**2) - (4 * a * c)

# Calcula a primeira raiz da esquaçao com +
x1 = -b + delta**0.5 / 2 * a

# Calcula a segunda raiz da esquaçao com -
x2 = -b - delta**0.5 / 2 * a

# retona o resultado das duas raizes
print('X1 é:', x1, '\nX2 é:', x2)
