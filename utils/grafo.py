from copy import deepcopy
from random import choice


class Grafo:
    """Grafo implementado con diccionarios de diccionarios"""

    def __init__(self, dirigido: bool, vertices: list | tuple = None) -> None:
        """
        Crear un grafo vacio.
        """
        self.es_dirigido = dirigido
        self._vertices = dict()
        if vertices is not None:
            for v in vertices:
                self.agregar_vertice(v)

    def agregar_vertice(self, vertice: any, sobrescribir: bool = True):
        """
        Agrega un vertice al grafo. Si el vertice ya existe, lanzara una excepcion
        """
        if vertice in self._vertices and not sobrescribir:
            raise ValueError(f"El vertice \"{vertice}\" ya existe")
        if vertice is None:
            raise ValueError("El vertice no puede ser None")

        self._vertices[vertice] = dict()

    def borrar_vertice(self, vertice: any) -> None:
        """
        Borra un vertice del grafo. Si el vertice no existe, lanzara una excepcion
        """
        if vertice not in self._vertices:
            raise ValueError(f"El vertice \"{vertice}\" no existe")

        for vertices in self._vertices.values():
            if vertice in vertices:
                del vertices[vertice]
        del self._vertices[vertice]

    def agregar_arista(self, origen: any, destino: any, peso: int = 1, sobrescribir: bool = True):
        """
        Agrega una arista al grafo. Si alguno de los vertices no existe, lanzara una excepcion
        """
        if origen not in self._vertices:
            raise ValueError(f"El vertice origen \"{origen}\" no existe")
        if destino not in self._vertices:
            raise ValueError(f"El vertice destino \"{destino}\" no existe")
        if destino in self._vertices[origen] and not sobrescribir:
            if self.es_dirigido:
                raise ValueError(f"La arista \"{origen}\" -> \"{destino}\" ya existe")
            raise ValueError(f"La arista \"{origen}\" - \"{destino}\" ya existe")

        self._vertices[origen][destino] = peso
        if not self.es_dirigido:
            self._vertices[destino][origen] = peso

    def borrar_arista(self, origen: any, destino: any):
        """
        Borra una arista del grafo. Si alguno de los vertices no existe, lanzara una excepcion
        """
        if origen not in self._vertices:
            raise ValueError(f"El vertice origen \"{origen}\" no existe")
        if destino not in self._vertices:
            raise ValueError(f"El vertice destino \"{destino}\" no existe")

        try:
            del self._vertices[origen][destino]
            if not self.es_dirigido:
                del self._vertices[destino][origen]
        except KeyError:
            if self.es_dirigido:
                raise ValueError(f"La arista \"{origen}\" -> \"{destino}\" no existe")
            raise ValueError(f"La arista \"{origen}\" - \"{destino}\" no existe")

    def vertices(self):
        """
        Devuelve una tupla con los vertices del grafo
        """
        return tuple(self._vertices)

    def adyacentes(self, vertice: any) -> tuple:
        """
        Devuelve una tupla con los vertices adyacentes al vertice pasado por parametro.
        """
        if vertice not in self._vertices:
            raise ValueError(f"El vertice \"{vertice}\" no existe")

        return tuple(self._vertices[vertice])

    def vertice_aleatorio(self) -> any:
        """
        Devuelve un vertice aleatorio del grafo
        """
        if len(self._vertices) == 0:
            return None
        return choice(self.vertices())

    def peso_arista(self, origen: any, destino: any) -> int:
        """
        Devuelve el peso de una arista
        """
        if origen not in self._vertices:
            raise ValueError(f"El vertice origen \"{origen}\" no existe")
        if destino not in self._vertices:
            raise ValueError(f"El vertice destino \"{origen}\" no existe")
        return self._vertices[origen][destino]

    def estan_conectados(self, origen, destino) -> bool:
        """
        Devuelve True si el origen y el destino estan conectados, False en caso contrario
        """
        if origen not in self._vertices:
            raise ValueError(f"El vertice origen \"{origen}\" no existe")
        if destino not in self._vertices:
            raise ValueError(f"El vertice destino \"{destino}\" no existe")
        return destino in self._vertices[origen]

    def limpiar(self) -> None:
        """
        Borra todos los vertices y aristas del grafo
        """
        self._vertices.clear()

    def copiar(self) -> "Grafo":
        """
        Devuelve una copia del grafo
        """
        return deepcopy(self)

    def __str__(self) -> str:
        return str(self._vertices)

    def __len__(self) -> int:
        return len(self._vertices)

    def __iter__(self) -> iter:
        return iter(self._vertices)

    def __eq__(self, other: "Grafo") -> bool:
        for vertice in self._vertices:
            if vertice not in other._vertices:
                return False
            for adyacente in self._vertices[vertice]:
                if adyacente not in other._vertices[vertice] or self._vertices[vertice][adyacente] != \
                        other._vertices[vertice][adyacente]:
                    return False
        return True
