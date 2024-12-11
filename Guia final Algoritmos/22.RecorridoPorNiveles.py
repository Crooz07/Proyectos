from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def recorrido_por_niveles(raiz):
    if raiz is None:
        return

    cola = deque([raiz])
    while cola:
        nodo_actual = cola.popleft()
        print(nodo_actual.valor, end=" ")

        if nodo_actual.izquierdo:
            cola.append(nodo_actual.izquierdo)
        if nodo_actual.derecho:
            cola.append(nodo_actual.derecho)


raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

print("Recorrido por niveles del árbol:")
recorrido_por_niveles(raiz)
