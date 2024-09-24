from utils import grafo as Grafo

def kruskal(grafo):  # O(E log V)  # genera un bosque de tendido minimo
    conjuntos = UnionFind(grafo.vertices())
    aristas = []  
    for v in grafo: # O(V + E)
        for w in grafo.adyacentes(v):
            aristas.append((v, w, grafo.peso_arista(v, w))) 
    aristas.sort(key=lambda x: x[2])  # O(E log V)
    arbol = Grafo(False)
    for v in grafo:  # O(V)
        arbol.agregar_vertice(v)
    for origen, destino, peso in aristas:  # O(E)
        if conjuntos.find(origen) == conjuntos.find(destino):  # O(1)
            continue
        arbol.agregar_arista(origen, destino, peso)
        conjuntos.union(origen, destino)  # O(log V)
    return arbol


class UnionFind:
    def __init__(self, elementos):
        self.groups = dict()
        for e in elementos:
            self.groups[e] = e

    def find(self, v):
        if self.groups[v] == v:
            return v
        real_group = self.find(self.groups[v])
        self.groups[v] = real_group
        return real_group

    def union(self, u, v):
        new_group = self.find(u)
        other = self.find(v)
        self.groups[other] = new_group


# El algoritmo de Kruskal es Greedy porque:
# En cada paso, selecciona la arista más pequeña posible que no forme un ciclo. Esta es una decisión localmente óptima que maximiza el progreso hacia la solución del MST, sin tener en cuenta las futuras aristas o cómo afectarán al resto del grafo.
# No reconsidera las decisiones previas; una vez que se añade una arista, esta permanece en el MST.
# El Algoritmo de Kruskal es Greedy porque, en cada paso, elige la arista más pequeña disponible que no forme un ciclo. Esta estrategia Greedy asegura que en cada momento se está añadiendo la arista de menor peso posible al MST, y gracias a la naturaleza del problema del árbol generador mínimo, esta estrategia local Greedy lleva a la solución global óptima.