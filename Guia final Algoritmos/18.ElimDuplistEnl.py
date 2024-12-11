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


class ListaSinDuplicados(ListaEnlazada):
    def eliminar_duplicados(self):
        elementos = set()
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato in elementos:
                anterior.siguiente = actual.siguiente
            else:
                elementos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente


lista = ListaSinDuplicados()
lista.agregar(1)
lista.agregar(2)
lista.agregar(2)
lista.agregar(3)
print("Lista con duplicados: [1, 2, 2, 3]")
lista.eliminar_duplicados()
print("Lista sin duplicados:", end=" ")
actual = lista.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()
