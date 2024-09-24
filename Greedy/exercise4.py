HORA_INICIO = 0
HORA_FINALIZACION = 1


def max_charlas(horarios_charlas):
    horarios_charlas.sort(key=lambda horarios_charla: horarios_charla[HORA_FINALIZACION]) # O(n log n)
    orden_sala = []
    fin_anterior = 0
    for inicio, fin in horarios_charlas: # O(n)
        if inicio >= fin_anterior:
            orden_sala.append((inicio, fin))
            fin_anterior = fin
    return orden_sala



horarios_charlas = [(2, 3), (1, 2), (5, 7), (6, 9), (2, 4)]
"""
def max_charlas(horarios_charlas):
    if (len(horarios_charlas) == 0):
        return []
    horarios_charlas.sort(key=lambda horarios_charla: horarios_charla[HORA_FINALIZACION])
    max_charlas = []

    max_charlas.append(horarios_charlas[0])
    for horarios_charla in horarios_charlas:
        if horarios_charla[HORA_INICIO] >= max_charlas[-1][HORA_FINALIZACION]:
            max_charlas.append(horarios_charla)
    return max_charlas

"""

# El algoritmo es greedy porque sigue el principio de tomar decisiones óptimas en cada paso basado en la información disponible en ese momento, sin considerar soluciones futuras. En este caso, siempre selecciona la charla que termina más pronto, lo cual parece ser la mejor elección en cada paso, sin necesidad de revisar las charlas que están más adelante en la lista.
# El criterio de selección de charlas es localmente óptimo: en cada paso se selecciona la charla que deja libre la sala lo más pronto posible, con la esperanza de que este enfoque también lleve a una solución globalmente óptima.
def main():
    print(max_charlas(horarios_charlas))

if __name__ == '__main__':
    main()
