class ColaCircular:
    def __init__(self, tamaño):
        self.items = [None] * tamaño
        self.tamaño = tamaño
        self.inicio = 0
        self.fin = -1
        self.num_elementos = 0

    def enqueue(self, item):
        if self.num_elementos < self.tamaño:
            self.fin = (self.fin + 1) % self.tamaño
            self.items[self.fin] = item
            self.num_elementos += 1

    def dequeue(self):
        if self.num_elementos > 0:
            elemento = self.items[self.inicio]
            self.items[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamaño
            self.num_elementos -= 1
            return elemento
        return None


cola_circular = ColaCircular(3)
cola_circular.enqueue(10)
cola_circular.enqueue(20)
cola_circular.enqueue(30)
print("Cola Circular dequeue:", cola_circular.dequeue())
