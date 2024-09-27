import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.grafo import Grafo

# Fuerza Bruta -------------------------------------------------------

def es_compatible_FB(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w :
                continue
            if (grafo.estan_conectados(v, w)):
                return False
    return True

def _ubicacion_FB(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n:
        return es_compatible_FB(grafo, puestos)
    if v_actual == len(grafo):
        return False
    
    puestos.add(vertices[v_actual])
    if _ubicacion_FB(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_FB(grafo, vertices, v_actual + 1, puestos, n)

def ubicacion_FB(grafo, n):
    puestos = set()
    _ubicacion_FB(grafo, grafo.vertices(), 0, puestos, n)
    return puestos

# Backtracking -------------------------------------------------------

def es_compatible_BT(grafo, puestos, ultimo_puesto):
    for w in puestos:
        if ultimo_puesto == w :
            continue
        if (grafo.estan_conectados(ultimo_puesto, w)):
            return False
    return True

def ya_no_llego_BT(grafo, puestos, v_actual, n):
    v_faltantes = len(grafo) - (v_actual + 1)
    if (len(puestos) + v_faltantes < n):
        return False
    return True

def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n:
        return es_compatible_BT(grafo, puestos)
    if v_actual == len(grafo):
        return False
    
    if es_compatible_BT(grafo, puestos, vertices[v_actual]) or ya_no_llego_BT(grafo, puestos, v_actual, n):
        return False
    
    puestos.add(vertices[v_actual])
    if _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)

def ubicacion_BT(grafo, n):
    puestos = set()
    _ubicacion_FB(grafo, grafo.vertices(), 0, puestos, n)
    return puestos




def main():


    grafo = Grafo(dirigido=True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    print(ubicacion_FB(grafo, 2))

    grafo = Grafo(dirigido=True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_arista("A", "B")
    print(ubicacion_FB(grafo, 2))

if __name__ == '__main__':
    main()