# Receba os valores em X e Y. Efetua a troca de seus valores e mostre seus conteúdos.
# declarar
X: int = 0
Y: int = 0
Z: int = 0
# incio
# recebe e mostra o valor de X
X = int(input('\nDigite um valor para X: '))
print('O valor de X é:', X)

# recebe e mostra o valor de Y
Y = int(input('\nDigite um valor para Y: '))
print('O valor de Y é:', Y)

# troca o valor de X com Y
Z = X
X = Y
Y = Z

# retorna os valores atualizados de X e Y
print('\nO Valor de X agora é:', X, '\nE o valor de Y agora é:', Y)
