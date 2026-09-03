"""
Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes.
Calcule o salário que serão as horas trabalhas x o valor por horas.
Calcule o salário líquido (=Salário bruto-desconto).
A cada dependente será acrescido R$100 no Salário Líquido. 
Exiba o salário a receber.
"""
# declarar
horatra: int = 0
valhora: float = 0
percedes: float = 0
descen: int = 0
salbrut: float = 0
salliq: float = 0
salreceb: float = 0
# inicio
# Recebe as horas trabalhadas
horatra = float(input('Digite quantas horas de trabalho: '))

# recebe o valor da hora
valhora = float(input('Digite o valor da hora: '))

# recebe o percentual de desconto
percedes = float(input('Digite o percentual de desconto: '))

# recebe o número de descendestes
descen = int(input('Digite quantos descendestes: '))

# calcula salário
salbrut = horatra*valhora

# calcula salário líquido
salliq = salbrut - (salbrut * (percedes / 100))

# calcula salário final
salreceb = salliq + (descen*100)

# retorna o salário final
print('O salário a receber é :', salreceb)
