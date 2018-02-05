#Diamantes e Areia
n = int(input())
for i in range(n):
    entrada = input()
    pilha = []
    cont = 0
    for c in entrada:
        if c == '.':
            continue
        if c == '<':
            pilha.append(c)
        else:
            if pilha:
                pilha.pop()
                cont+=1
    print(cont)


