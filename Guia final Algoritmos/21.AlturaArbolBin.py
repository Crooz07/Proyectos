class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def altura_arbol(nodo):
    if nodo is None:
        return 0

    altura_izquierda = altura_arbol(nodo.izquierdo)
    altura_derecha = altura_arbol(nodo.derecho)

    return max(altura_izquierda, altura_derecha) + 1


raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)

print("Altura del árbol:", altura_arbol(raiz))
