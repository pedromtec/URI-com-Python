from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    fila = deque()
    for num in range(1, n+1):
        fila.append(num)
    descartadas = []
    while len(fila) >= 2:
        descartadas.append(fila.popleft())
        fila.append(fila.popleft())
    print("Discarded cards: ", end="")
    for i in range(len(descartadas)-1):
        print("%d, "%descartadas[i], end="")
    print(descartadas[len(descartadas)-1])
    print("Remaining card: %d"%fila[0])
