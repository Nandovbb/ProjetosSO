# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia
# declarar
valorI: int=0
dias: int=0
gramas: int=0
#inicio
#recebe quantos quilos de alimento
valorI = int(input('Digite quantos quilos de alimento: '))

#converte quilos pars gramas
gramas= 1000*valorI

#contas quantos dias 
dias= gramas/50

#retorna quantos dias vai durar
print('Esse alimento vai durar:' , dias , 'dias.')