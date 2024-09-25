

def precios_inflacion(R):
    R.sort(reverse=True)
    min_precio = 0
    for i in range(len(R)):
        min_precio += R[i] ** (i+1)
    return min_precio



# En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

def precios_deflacion(R):
    R.sort()
    min_precio = 0
    for i in range(0, len(R)):
        min_precio += (R[i] / (2**i))
    return min_precio

