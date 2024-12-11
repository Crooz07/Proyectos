class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0


pila = Pila()
pila.push(10)
pila.push(20)
print("Pila pop:", pila.pop())
print("Pila peek:", pila.peek())
