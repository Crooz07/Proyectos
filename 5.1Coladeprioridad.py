class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nodo al final de la lista."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __iter__(self):
        """Iterador para recorrer la lista."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traverse(self):
        """Usa el iterador para recorrer la lista."""
        return [data for data in self]

    def __str__(self):
        """Representación en cadena usando el iterador."""
        return " -> ".join(str(data) for data in self)

    def __len__(self):
        """Devuelve la longitud de la lista usando el iterador."""
        return sum(1 for _ in self)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

print("Recorrido:", ll.traverse())
print("Cadena:", str(ll))
print("Longitud:", len(ll))
