while True:
    n = int(input())
    if n == 0:
        break
    while True:
        saida = list(map(int, input().split()))
        if saida[0] == 0:
            break
        pilha = []
        i = 0
        for vagao in range(1, n+1):
            pilha.append(vagao)
            while pilha and pilha[len(pilha)-1] == saida[i]:
                i+=1
                pilha.pop()
        if pilha:
            print("No")
        else:
            print("Yes")
    print()


                
        
    
