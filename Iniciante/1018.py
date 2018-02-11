# Problema -> Cédulas
n = int(input())
valor_lido = n
nota_100 = n//100
n%=100
nota_50 = n//50
n%=50
nota_20 = n//20
n%=20
nota_10 = n//10
n%=10
nota_5 = n//5
n%=5
nota_2 = n//2
n%=2
nota_1 = n
print(valor_lido)
print("{} nota(s) de R$ 100,00".format(nota_100))
print("{} nota(s) de R$ 50,00".format(nota_50))
print("{} nota(s) de R$ 20,00".format(nota_20))
print("{} nota(s) de R$ 10,00".format(nota_10))
print("{} nota(s) de R$ 5,00".format(nota_5))
print("{} nota(s) de R$ 2,00".format(nota_2))
print("{} nota(s) de R$ 1,00".format(nota_1))
