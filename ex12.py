# declarar
nasc: int = 0
ano: int = 0
conano: int = 0
# inicio
# recebe o ano de nascimento
nasc = int(input('Digite seu ano de nascimento: '))

# recebe o ano atual
ano = int(input('Digite o atual ano: '))

# faz a conta de quantos anos essa pessoa tem
conano = ano-nasc

# Soma 17 anos a idade da pessoa
conano = conano+17

# retona a idade da pessoa +17
print('Você terá', conano, 'anos daqui a 17 anos')