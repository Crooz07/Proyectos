class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        # Inserción rápida en O(1)
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise Exception("PriorityQueue is empty. Cannot remove.")
        # Búsqueda y eliminación del elemento de mayor prioridad en O(n)
        max_index = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[max_index]:
                max_index = i
        return self.items.pop(max_index)


# Programa de prueba
pq = PriorityQueue()
pq.insert(10)
pq.insert(5)
pq.insert(30)
print("Removed highest priority:", pq.remove())  # Debería mostrar 30
print("Removed next highest priority:", pq.remove())  # Debería mostrar 10
