# Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1.3$a. m.
# declarar
pou: float = 0

# inicio
# recebe o valor na poupança
pou = float(input('Digite o valor na poupança: '))

# calcula o rendimento de 1,3%
pou = pou+(pou*0.013)

# mostra o valor da poupança com um rendimento de 1,3%
print('O valor após 1 mês seria de:', pou)
