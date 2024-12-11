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

class ListaFusionable(ListaEnlazada):
    def fusionar(self, otra_lista):
        dummy = Nodo(0) 
        actual = dummy
        a, b = self.cabeza, otra_lista.cabeza
        while a and b:
            if a.dato <= b.dato:
                actual.siguiente = a
                a = a.siguiente
            else:
                actual.siguiente = b
                b = b.siguiente
            actual = actual.siguiente
        actual.siguiente = a if a else b
        self.cabeza = dummy.siguiente


print("== Invertir Lista ==")
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
print("\n")

print("== Eliminar Duplicados ==")
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
print("\n")

print("== Fusionar Listas ==")
lista1 = ListaFusionable()
lista2 = ListaFusionable()
lista1.agregar(1)
lista1.agregar(3)
lista2.agregar(2)
lista2.agregar(4)
print("Lista 1: [1, 3]")
print("Lista 2: [2, 4]")
lista1.fusionar(lista2)
print("Lista fusionada:", end=" ")
actual = lista1.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()
