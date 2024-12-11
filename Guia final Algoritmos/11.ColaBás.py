class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def esta_vacia(self):
        return len(self.items) == 0


cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
print("Cola dequeue:", cola.dequeue())
print("Cola peek:", cola.peek())
