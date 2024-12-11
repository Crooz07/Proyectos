# 12. Simular una Fila de Banco
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


def fila_banco(clientes):
    cola = Cola()
    for cliente in clientes:
        cola.enqueue(cliente)
    while not cola.esta_vacia():
        print(f"Cliente en ventanilla: {cola.dequeue()}")


fila_banco(["Cliente 1", "Cliente 2", "Cliente 3"])
