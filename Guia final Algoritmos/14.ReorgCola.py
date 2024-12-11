class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def peek(self):
        if not self.esta_vacia():
            return self.items[0]
        return None


def reorganizar_cola(cola):
    pares = []
    impares = []
    while not cola.esta_vacia():
        num = cola.dequeue()
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    for num in pares + impares:
        cola.enqueue(num)
    return cola


cola_reorganizar = Cola()
cola_reorganizar.enqueue(3)
cola_reorganizar.enqueue(2)
cola_reorganizar.enqueue(4)
cola_reorganizar.enqueue(1)
reorganizar_cola(cola_reorganizar)

print("Cola reorganizada:")
while not cola_reorganizar.esta_vacia():
    print(cola_reorganizar.dequeue())
