def cambio_minimo(monedas, monto):
    min_cambio = []
    monedas.sort(reverse=True)  # Ordenamos las monedas de mayor a menor valor O(n log n)
    
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            min_cambio.append(moneda)
    
    return min_cambio

"""

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    min_cambio = []
    for moneda in monedas:
        cantidad_cambio, monto = divmod(monto, moneda)
        for _ in range(cantidad_cambio):
            min_cambio.append(moneda)
        if monto == 0:
            break
    return min_cambio

"""

# Ordenación de las monedas: La complejidad de la función sort() es O(n log n), donde n es el número de monedas en el sistema.
# Selección de las monedas: El bucle for recorre las n monedas y el bucle interno while se ejecuta tantas veces como sea necesario hasta que el cambio sea 0. 
# En el peor caso, este bucle puede ejecutarse hasta que la cantidad se reduzca a 0, lo que ocurriría en 𝑂(c/m) iteraciones, donde c es la cantidad objetivo y m es la moneda más pequeña. 
# Entonces, el proceso de selección tiene una complejidad de O(n + c), siendo c la cantidad de cambio a dar.
# Por lo tanto, la complejidad queda como O(n log n + c)

# El algoritmo Greedy funciona tomando decisiones localmente óptimas, es decir, selecciona la moneda de mayor valor en cada paso, con la esperanza de minimizar la cantidad total de monedas. 
# En sistemas como el nuestro, con monedas que son múltiplos unas de otras, esta estrategia Greedy garantiza una solución óptima.

# El algoritmo Greedy encuentra la solución óptima en sistemas monetarios como el nuestro (donde cada moneda es múltiplo de la siguiente menor), pero no siempre es óptimo en todos los sistemas monetarios.
# Contraejemplo de un sistema no óptimo:
# Consideremos un sistema monetario ficticio con monedas de valores 1, 3, 4, y supongamos que necesitamos dar un cambio de 6.
# Este algoritmo nos da como resultado 4, 1 y 1. Cuando la mejor opción es 3 y 3.
def main():
    print(cambio_minimo([10, 100, 200], 550))

if __name__ == '__main__':
    main()