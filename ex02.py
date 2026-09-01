# declarar
salario: float = 0.0
reajuste: float = 0.0
# inicio
# recebe o valor do salário
salario = float(input("Digite o salário: "))

# faz o cálculo do reajuste
reajuste = salario + (salario * 0.15)

# retorna o reajuste do salário
print("O salário do funcionário é: ", reajuste)
