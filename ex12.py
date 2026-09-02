# Receba o ano de nascimento e ano atual. Calcule e mostre a idade e quantos anos terá daqui daqui a 17 anos
# declarar
nasc: int = 0
ano: int = 0
idade: int=0
idade17: int = 0
# inicio
# recebe o ano de nascimento
nasc = int(input('Digite seu ano de nascimento: '))

# recebe o ano atual
ano = int(input('Digite o atual ano: '))

# faz a conta de quantos anos essa pessoa tem
idade = ano-nasc

# Soma 17 anos a idade da pessoa
idade17 = idade+17

# retona a idade da pessoa +17
print('Você tem:', idade, '\nE daqui a 17 anos terá:', idade17)
