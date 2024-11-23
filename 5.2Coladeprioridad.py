class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, data, priority):
        """Inserta un elemento en la cola según su prioridad."""
        new_node = PriorityNode(data, priority)
        if not self.head or priority < self.head.priority:
            # Insertar al inicio
            new_node.next = self.head
            self.head = new_node
        else:
            # Insertar en el lugar correcto
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self):
        """Elimina el elemento con la menor prioridad."""
        if self.head:
            removed = self.head
            self.head = self.head.next
            return removed.data
        raise IndexError("remove from empty queue")

    def is_empty(self):
        """Comprueba si la cola está vacía."""
        return self.head is None

    def __str__(self):
        """Representación en cadena."""
        elements = []
        current = self.head
        while current:
            elements.append(f"({current.data}, {current.priority})")
            current = current.next
        return " -> ".join(elements)


pq = PriorityQueue()
pq.insert("A", 3)
pq.insert("B", 1)
pq.insert("C", 2)

print("Cola de prioridad:", pq)
print("Eliminar:", pq.remove())
print("Cola actual:", pq)
