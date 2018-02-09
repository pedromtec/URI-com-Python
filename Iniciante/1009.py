# Problema ->  Salário com Bônus
nome = input()
salario_fixo = float(input())
vendas_efetuadas = float(input())
total = salario_fixo + vendas_efetuadas*0.15
print("TOTAL = R$ %.2f"%total)