# Problema -> Idade em Dias
dias = int(input())
anos =  dias // 365
dias %= 365
meses = dias//30
dias%=30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))
