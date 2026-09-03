# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12km/l. Receber o tempo de percurso e a velocidade média.
# declarar
tempo: int = 0
velocidade: int = 0
litros: int = 0
# inicio
# recebe o tempo de percurso
tempo = int(input('Digite quanto tempo de viagem: '))

# recebe a velocidade média
velocidade = int(input('Digite a velocidade média: '))

# calcula quantos litros gastos
litros = (tempo * velocidade)/12

# retorna quantos litros foram gastos
print('Foram gastos ', int(litros), 'litros nessa viagem')
