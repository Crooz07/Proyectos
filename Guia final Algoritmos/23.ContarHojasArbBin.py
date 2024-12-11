class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def contar_hojas(nodo):
    if nodo is None:
        return 0

    if nodo.izquierdo is None and nodo.derecho is None:
        return 1

    return contar_hojas(nodo.izquierdo) + contar_hojas(nodo.derecho)


raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

print("Número de hojas en el árbol:", contar_hojas(raiz))
