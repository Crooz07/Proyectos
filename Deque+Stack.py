class DequeStack:
    def __init__(self):
        self.deque = Deque()

    def is_empty(self):
        return self.deque.is_empty()

    def is_full(self):
        return self.deque.is_full()

    def push(self, item):
        self.deque.insert_right(item)

    def pop(self):
        return self.deque.remove_right()

    def peek(self):
        return self.deque.peek_right()


# Programa de prueba
stack = DequeStack()
stack.push(10)
stack.push(20)
print("Top element after pushes:", stack.peek())  # Debería mostrar 20
stack.pop()  # Quita 20
print("Top element after pop:", stack.peek())  # Debería mostrar 10
