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

    def eliminar(self, dato):
        if not self.cabeza:
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False


lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
print("Lista original: [1, 2, 3]")
print("Buscar 2 en la lista:", lista.buscar(2))
lista.eliminar(2)
print("Lista después de eliminar 2:", end=" ")
actual = lista.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()
