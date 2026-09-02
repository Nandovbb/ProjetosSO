# Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
# declarar
comp: int = 0
lar: int = 0
alt: int = 0
vol: int = 0
# inicio
# recebe o comprimento do paralelepípedo
comp = int(input('Digite o comprimento do paralelepípedo: '))

# recebe a largura do paralelepípedo
lar = int(input('Digite a largura do paralelepípedo: '))

# recebe a aluta do paralelepípedo
alt = int(input('Digite o altura do paralelepípedo: '))

# calcula o volume do paralelepípedo
vol = comp*lar*alt

# retorna o valor do volume
print(vol)
