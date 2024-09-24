from heapq import heappush, heappop


def dijkstra(grafo, origen, destino=None):
    distancia = dict()
    padre = dict()
    q = []
    heappush(q, (0, origen))
    padre[origen] = None
    for v in grafo:
        distancia[v] = float("inf")
    distancia[origen] = 0

    while len(q) > 0:
        _, v = heappop(q)
        for w in grafo.adyacentes(v):
            distancia_por_aca = distancia[v] + grafo.peso_arista(v, w)
            if distancia_por_aca < distancia[w]:
                distancia[w] = distancia_por_aca
                padre[w] = v
                heappush(q, (distancia_por_aca, w))
                if w is not None and w == destino:
                    return distancia, padre
    return distancia, padre


# Es Greedy porque
# En cada iteración, toma la decisión localmente óptima, eligiendo el vértice que parece tener la distancia más corta en ese momento.
# No reconsidera las decisiones anteriores, asumiendo que, una vez que un vértice ha sido procesado, su distancia mínima no puede ser mejorada.
# En resumen, el Algoritmo de Dijkstra es Greedy porque toma decisiones locales, eligiendo siempre el vértice con la distancia más corta conocida en cada paso, y espera en que esta elección llevará a la solución óptima