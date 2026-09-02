# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia
# declarar
valorI: float=0
dias: float=0
gramas: float=0
#inicio
#recebe quantos quilos de alimento
valorI = float(input('Digite quantos quilos de alimento: '))

#converte quilos pars gramas
gramas= 1000*valorI

#contas quantos dias 
dias= gramas//50

#retorna quantos dias vai durar
print('Esse alimento vai durar:' , int(dias) , 'dias.')