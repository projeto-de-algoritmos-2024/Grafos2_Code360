from os import *
from sys import *
from collections import *
from math import *
import heapq

def getMinimumCost(n, m, connections):
    custo = 0
    arestas_usadas = 0
    grafo = defaultdict(list)

    for u, v, w in connections:  # u -> CO / v -> CD w -> custo
        grafo[u].append((w, v))
        grafo[v].append((w, u))

    min_heap = [(0, 1)]
    visitados = set()

    while min_heap:
        custo_no, u = heapq.heappop(min_heap)

        if u in visitados:
            continue
        
        visitados.add(u)
        custo += custo_no
        arestas_usadas += 1

        for custo_aresta, v in grafo[u]:
            if v not in visitados:
                heapq.heappush(min_heap, (custo_aresta, v))


    if n == arestas_usadas:
        return custo
    return -1


    pass