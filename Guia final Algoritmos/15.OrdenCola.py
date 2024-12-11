from queue import Queue


def ordenar_cola(cola):
    elementos = []
    while not cola.empty():
        elementos.append(cola.get())
    elementos.sort()
    for elemento in elementos:
        cola.put(elemento)
    return cola


cola = Queue()
cola.put(3)
cola.put(1)
cola.put(4)
cola.put(2)
print("Cola original: [3, 1, 4, 2]")
ordenar_cola(cola)
print("Cola ordenada:", end=" ")
while not cola.empty():
    print(cola.get(), end=" ")
print()
