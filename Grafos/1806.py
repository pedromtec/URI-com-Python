# Problema -> Agente 004

from sys import stdin, stdout
from heapq import *

INF = 1000000000000

def dijkstra(grafo, origem):
	tam = len(grafo)
	seen = [False] * tam
	dist = [INF] * tam
	pq = []
	dist[origem] = 0
	heappush(pq, (dist[origem], origem))
	while pq:
		v = heappop(pq)[1]
		if seen[v]:
			continue
		seen[v] = True
		for u, d in grafo[v]:
			if dist[v] + d < dist[u]:
				dist[u] = dist[v]+d
				heappush(pq, (dist[u], u))
	return dist

if __name__ == "__main__":
	n,c,s,b = map(int, stdin.readline().split())
	grafo = [0]
	for i in range(1, n+1):
		grafo.append([])
	for i in range(c):
		a,b,v = map(int, stdin.readline().split())
		grafo[a].append((b, v))
		grafo[b].append((a, v))
	rotas_criminosos = []
	for i in range(s):
		a,b,v = map(int, stdin.readline().split())
		rotas_criminosos.append((a,b,v))
	lugares = list(map(int, stdin.readline().split()))
	k, f = map(int, stdin.readline().split())
	distancias = dijkstra(grafo, f)
	dist_bino = distancias[k]
	for a,b,v in rotas_criminosos:
		grafo[a].append((b, v))
		grafo[b].append((a, v))
	distancias_criminosos = dijkstra(grafo, f)
	eliminados=0
	for lugar in lugares:
		if distancias_criminosos[lugar] <= dist_bino:
			eliminados+=1
	print(eliminados)
