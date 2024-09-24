from heapq import heappush, heappop
from utils import grafo as Grafo

def prim(grafo):  # O(E log V)
    v = grafo.vertice_aleatorio()
    visitados = set()
    visitados.add(v)
    q = []
    for w in grafo.adyacentes(v):
        heappush(q, (grafo.peso_arista(v, w), v, w))

    arbol = Grafo(False)
    for v in grafo:
        arbol.agregar_vertice(v)

    while len(q) > 0:
        peso, v, w = heappop(q)
        if w in visitados:
            continue
        visitados.add(w)
        arbol.agregar_arista(v, w, peso)
        for x in grafo.adyacentes(w):
            if x not in visitados:
                heappush(q, (grafo.peso_arista(w, x), w, x))
    return arbol


# Es Greedy porque
# En cada paso, selecciona la arista más pequeña que conecta el árbol parcial (MST) con un nuevo vértice. Esta es una decisión localmente óptima que se espera que conduzca al árbol generador mínimo global.
# Las decisiones tomadas en cada iteración se basan solo en el estado actual del árbol parcial y no consideran el impacto futuro. Una vez que se selecciona una arista, no se reconsidera.
# En resumen, el Algoritmo de Prim es Greedy porque selecciona en cada paso la arista de menor peso posible que conecte el árbol parcial con un nuevo vértice. Esta estrategia asegura que, en cada momento, se está tomando una decisión localmente óptima, y gracias a las propiedades de los árboles generadores mínimos, esta estrategia local Greedy conduce a una solución global óptima.