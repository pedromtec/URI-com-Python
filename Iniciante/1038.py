#Lanche

cod, qtd = map(int, input().split())

res = 0

if cod == 1:
    res = qtd * 4.00
if cod == 2:
    res = qtd * 4.50
if cod == 3:
    res = qtd * 5.00
if cod == 4:
    res = qtd * 2.00
if cod == 5:
    res = qtd * 1.50

print("Total: R$ %.2f"%res)
