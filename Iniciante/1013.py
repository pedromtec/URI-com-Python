#O Maior
a,b,c = map(int, input().split())
maior = (a+b+abs(a-b))//2
maior = (maior+c+abs(maior-c))//2
print("{} eh o maior".format(maior))
