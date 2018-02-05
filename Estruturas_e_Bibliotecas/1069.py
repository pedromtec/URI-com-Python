n = int(input())
for i in range(n):
    entrada = input()
    pilha = []
    cont = 0
    for c in entrada:
        if c == '<':
            pilha.append(c)
        elif c == '>' and pilha:
            pilha.pop()
            cont+=1
    print(cont)


