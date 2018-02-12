# Problema -> Notas e Moedas
n = float(input())
moeda = int((n-int(n)) * 100)
nota = int(n)
nota_100 = nota//100
nota%=100
nota_50 = nota//50
nota%=50
nota_20 = nota//20
nota%=20
nota_10 = nota//10
nota%=10
nota_5 = nota//5
nota%=5
nota_2 = nota//2
nota%=2
moeda+= (nota * 100)
moeda_1 = moeda//100
moeda%=100
moeda_050 = moeda//50
moeda%=50
moeda_025 = moeda//25
moeda%=25
moeda_010 = moeda//10
moeda%=10
moeda_005 = moeda//5
moeda%=5
moeda_001 = moeda

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(nota_100))
print("{} nota(s) de R$ 50.00".format(nota_50))
print("{} nota(s) de R$ 20.00".format(nota_20))
print("{} nota(s) de R$ 10.00".format(nota_10))
print("{} nota(s) de R$ 5.00".format(nota_5))
print("{} nota(s) de R$ 2.00".format(nota_2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moeda_1))
print("{} moeda(s) de R$ 0.50".format(moeda_050))
print("{} moeda(s) de R$ 0.25".format(moeda_025))
print("{} moeda(s) de R$ 0.10".format(moeda_010))
print("{} moeda(s) de R$ 0.05".format(moeda_005))
print("{} moeda(s) de R$ 0.01".format(moeda_001))

