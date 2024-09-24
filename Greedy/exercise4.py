HORA_INICIO = 0
HORA_FINALIZACION = 1


def max_charlas(horarios_charlas):
    horarios_charlas.sort(key=lambda horarios_charla: horarios_charla[HORA_FINALIZACION])
    orden_sala = []
    fin_anterior = 0
    for inicio, fin in horarios_charlas:
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
        if max_charlas[-1][HORA_FINALIZACION] <= horarios_charla[HORA_INICIO]:
            max_charlas.append(horarios_charla)
    return max_charlas

"""
def main():
    print(max_charlas(horarios_charlas))

if __name__ == '__main__':
    main()
