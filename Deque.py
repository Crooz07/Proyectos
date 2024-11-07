class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        # Suponemos que la deque no tiene un límite de tamaño fijo
        return False

    def insert_left(self, item):
        self.items.insert(0, item)

    def insert_right(self, item):
        self.items.append(item)

    def remove_left(self):
        if self.is_empty():
            raise Exception("Deque is empty. Cannot remove from left.")
        return self.items.pop(0)

    def remove_right(self):
        if self.is_empty():
            raise Exception("Deque is empty. Cannot remove from right.")
        return self.items.pop()

    def peek_left(self):
        if self.is_empty():
            raise Exception("Deque is empty. Cannot peek left.")
        return self.items[0]

    def peek_right(self):
        if self.is_empty():
            raise Exception("Deque is empty. Cannot peek right.")
        return self.items[-1]


# Programa de prueba
deque = Deque()
deque.insert_left(1)
deque.insert_right(2)
deque.insert_left(3)

print("Left peek:", deque.peek_left())  # Debería mostrar 3
print("Right peek:", deque.peek_right())  # Debería mostrar 2

deque.remove_left()  # Quita 3
deque.remove_right()  # Quita 2
print("Left peek after removals:", deque.peek_left())  # Debería mostrar 1
