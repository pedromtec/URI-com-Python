# Problema -> Cálculo Simples
cod_peca1, numero_de_pecas1, valor_peca1 = map(float, input().split())
cod_peca2, numero_de_pecas2, valor_peca2 = map(float, input().split())
total = numero_de_pecas1*valor_peca1 + numero_de_pecas2*valor_peca2
print("VALOR A PAGAR: R$ %.2f"%(total))
