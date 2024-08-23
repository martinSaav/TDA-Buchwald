def indice_mas_bajo(alumnos):
    return _indice_mas_bajo(alumnos, 0, len(alumnos) - 1)


def _indice_mas_bajo(alumnos, inicio, fin):
    if (inicio >= fin):
        return -1

    mitad = (inicio + fin) // 2

    if (alumnos[mitad-1].altura > alumnos[mitad].altura < alumnos[mitad+1].altura):
        return mitad
    if (alumnos[mitad].altura < alumnos[mitad+1].altura):
        return _indice_mas_bajo(alumnos, inicio, mitad)
    return _indice_mas_bajo(alumnos, mitad + 1, fin)


def validar_mas_bajo(alumnos, indice):
    return (alumnos[indice-1].altura > alumnos[indice].altura < alumnos[indice+1].altura)
