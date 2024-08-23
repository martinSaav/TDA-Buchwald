---
math: true
---

# División y Conquista
{:.no_toc}


## Contenidos
{:.no_toc}

1. TOC
{:toc}


## Ejercicio resuelto

### Solución

#### Demostración del orden

## Ejercicios propuestos

1.  (★) Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y _casi ordenado_ (todos los elementos se 
    encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar su complejidad temporal.

1.  (★) Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. Este código se encontraba funcionando 
    pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario.
    De esta manera, el arreglo tendrá la forma `[1, 1, 1, ..., 0, 0, ...]` (es decir, _unos seguidos de ceros_). Se pide:
    a. una función de orden $$\mathcal{O}(\log n)$$ que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer 
    rápidamente en qué modificación del código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), debe devolver -1.
    b. demostrar con el Teorema Maestro que la función es, en efecto, $$\mathcal{O}(\log n)$$.

    Ejemplos:

        [1, 1, 0, 0, 0] →  2
        [0, 0, 0, 0, 0] →  0
        [1, 1, 1, 1, 1] → -1

1.  (★) Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de
    un número $$n$$, en tiempo $$\mathcal{O}(\log n)$$. Por ejemplo, para $$n = 10$$ debe devolver 3, y para $$n = 25$$
    debe devolver 5. Justificar el orden del algoritmo.

1.  (★) Se tiene un arreglo de $$N >= 3$$ elementos en forma de pico, esto es: estrictamente creciente hasta una
    determinada posición $$p$$, y estrictamente decreciente a partir de ella (con $$0 \lt p \lt N - 1$$). Por ejemplo,
    en el arreglo `[1, 2, 3, 1, 0, -2]` la posición del pico es $$p = 2$$. Se pide:
    a. Implementar un algoritmo de división y conquista de orden $$\mathcal{O}(\log n)$$ que encuentre la posición
    $$p$$ del pico.
    b. Justificar el orden del algoritmo mediante el teorema maestro.
    {:.lower_alpha}

1.  (★) Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

1.  (★) Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con 
    un orden de complejidad mejor que $$\mathcal{O}(n^2)$$. Justificar el orden del algoritmo mediante el teorema maestro.

1.  (★★) Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división 
    y conquista, con un orden de complejidad mejor que $$\mathcal{O}(n^2)$$. Justificar el orden del algoritmo mediante el 
    teorema maestro. Se puede asumir que ningún par de puntos tienen la misma coordenada x o y.

1.  (★) Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente 
    ordenado de menor a mayor. El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de 
    inversiones necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad 
    mejor que $$\mathcal{O}(n^2)$$. Justificar el orden del algoritmo mediante el teorema maestro.

1.  (★★★) Implementar una función, que utilice división y conquista, de orden $$\mathcal{O}(n \log n)$$ 
    que dado un arreglo de $$n$$ números enteros devuelva `true` o `false` según si existe algún elemento que aparezca
    más de la mitad de las veces. Justificar el orden de la solución. Ejemplos:

        [1, 2, 1, 2, 3] -> false
        [1, 1, 2, 3] -> false
        [1, 2, 3, 1, 1, 1] -> true
        [1] -> true

    _Aclaración_: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente,
    o incluso se puede realizar más rápido utilizando una tabla de hash. Para cumplir con la consigna,
    resolver **sin ordenar el arreglo ni con tabla de hash**, sino puramente por división y conquista.

1.  (★★★★) Resolver el ejercicio anterior, por división y conquista, en orden $$\mathcal{O}(n)$$, 
    dada la misma aclaración. Justificar el orden de la solución.

1.  (★★★★) Implementar una función, que utilice división y conquista, de orden $$\mathcal{O}(n)$$
    que dado un arreglo de $$n$$ números enteros devuelva `true` o `false` según si existe algún elemento que aparezca
    más de dos tercios de las veces. Justificar el orden de la solución.

1.  (★★★) Tenemos un arreglo de tamaño `2n` de la forma `{C1, C2, C3, … Cn, D1, D2, D3, … Dn}`, 
	tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, `n` 
	también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo 
	de tal forma que quede con la forma `{C1, D1, C2, D2, C3, D3, …, Cn, Dn}`, **sin utilizar 
	espacio adicional** (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.

	_Pista_: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos 
	(`{C1, C2, D1, D2}`). Luego, pensar a partir de allí el caso de 8 elementos, etc...
	para encontrar el patrón. 

1.  (★★★) Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo 
    contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo.
    Ejemplos:

        [5, 3, 2, 4, -1] →  [5, 3, 2, 4]
        [5, 3, -5, 4, -1] →  [5, 3]
        [5, -4, 2, 4, -1] → [5, -4, 2, 4]
        [5, -4, 2, 4] → [5, -4, 2, 4]

1.	(★★) Debido a la trágica situación actual, es necesario realizar tests para detectar
	si alguna persona está contagiada de COVID-19. El problema es que los insumos
	tienden a ser bastante caros, y no vivimos en un país al que los recursos le sobren. 

	Supongamos que por persona se toma más de una muestra (lo cual es cierto, pero a fines
	del ejercicio supongamos que son muchas muestras), y que podemos realizar un testeo a más 
	de una persona al mismo tiempo mezclando las muestras (lo cual también es cierto): 
	determinamos un conjunto de personas a testear, obtenemos una muestra de cada una de ellas,
	las "juntamos", y al conjunto le realizamos el test. Si el test resulta negativo, 
	implica que todas las personas testeadas en conjunto resultaron negativas. Si resulta 
	positivo, implica que al menos una de las personas testedas resulta positiva. 

	Suponer que existe una función `pcr(grupo)`, que devuelve `true` si al menos una persona
	del `grupo` es COVID-positivo, y `false` en caso contrario (los `grupos` pueden estar
	formados por 1 o más personas). Suponer que la positividad es extremadamente baja, e inclusive
	pueden suponer que va a haber una única persona contagiada (por simplicidad). 

	Implementar un algoritmo que dado un conjunto de `n` personas, devuelva la o las personas
	contagiadas, utilizando la menor cantidad de tests posibles (considerando la notación Big Oh).
	En dicha notación, ¿cuántos tests se estarán utilizando?

	Pueden considerar que habrá una única persona contagiada, pero esto no cambiará el análisis
	a realizar. 
	
1. 	(★★) Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo `[a, b]`, 
	y que en el punto `a` es positiva y en el punto `b` es negativa (o viceversa), necesariamente
	debe haber (al menos) una raíz en dicho intervalo. Implementar una función 
	raiz que reciba una función (univariable) y los extremos mencionados a y b,
	y devuelva una raíz dentro de dicho intervalo (si hay más de una, 
	simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del
	largo del intervalo `[a, b]`. Asumir que por más que se esté trabajando con números enteros, 
	hay raíz en dichos valores: Se puede trabajar con `floats`, y el algoritmo será equivalente, 
	simplemente se plantea con `ints` para no generar confusiones con la complejidad.
	Justificar la complejidad de la función implementada.

1.  (★) Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la _Royal British Shipping & Something_, 
    que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron
    en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que
    los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es
    que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente
    la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya
    verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. 
    Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

    a. Escribir un algoritmo de división y conquista, para determinar cuál es la verdadera joya de la corona. Suponer que hay una función 
    `balanza(grupo_de_joyas1, grupo_de_joyas2)` que devuelve 0 si ambos grupos pesan lo mismo, mayor a 0 si
    el `grupo1` pesa más que el `grupo2`, y menor que 0 si pasa lo contrario, y realiza esto en tiempo 
    constante.
    b. Indicar y justificar (adecuadamente) la complejidad de la función implementada. 

{::options toc_levels="2" /}
