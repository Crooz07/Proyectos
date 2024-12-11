class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if not self.raiz:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo:
                self._insertar(nodo.izquierdo, dato)
            else:
                nodo.izquierdo = NodoArbol(dato)
        else:
            if nodo.derecho:
                self._insertar(nodo.derecho, dato)
            else:
                nodo.derecho = NodoArbol(dato)

    def inorden(self):
        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierdo)
                print(nodo.dato, end=" ")
                recorrer(nodo.derecho)
        recorrer(self.raiz)
        print()


arbol = ArbolBinario()
arbol.insertar(3)
arbol.insertar(1)
arbol.insertar(4)
arbol.insertar(2)
print("Árbol binario en inorden:", end=" ")
arbol.inorden()
