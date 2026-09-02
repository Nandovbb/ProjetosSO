# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3 ângulo
# declarar
ang1: int=0
ang2: int=0
ang3: int=0
#inicio
#recebe o valor do primeiro ângulo
ang1 = int(input('Digite o valor do primeiro ângulo: '))

#recebe o valor do segundo ângulo
ang2 = int(input('Digite o valor do segundo ângulo: '))

#calcula o valor do terceiro ângulo
ang3 = (180-ang1-ang2)

#retorna o valor o terceiro ângulo
print('O valor do terceiro ângulo é:', ang3)