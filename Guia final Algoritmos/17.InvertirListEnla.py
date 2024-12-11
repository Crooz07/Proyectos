class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo


class ListaEnlazadaInvertible(ListaEnlazada):
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior


lista = ListaEnlazadaInvertible()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
print("Lista original: [1, 2, 3]")
lista.invertir()
print("Lista invertida:", end=" ")
actual = lista.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()
