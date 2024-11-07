class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full. Cannot push.")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty. Cannot pop.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty. Cannot peek.")
        return self.items[-1]


# Programa de prueba
stack = Stack(3)
try:
    stack.push(1)
    stack.push(2)
    stack.push(3)
    # Intentamos agregar un cuarto elemento en una pila de tamaño 3
    stack.push(4)
except Exception as e:
    print(e)  # Esto imprimirá "Stack is full. Cannot push."

try:
    # Quitamos todos los elementos
    stack.pop()
    stack.pop()
    stack.pop()
    # Intentamos quitar un elemento de una pila vacía
    stack.pop()
except Exception as e:
    print(e)  # Esto imprimirá "Stack is empty. Cannot pop."
