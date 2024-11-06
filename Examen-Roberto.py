class ColaEspecial ():
    def __init__(self, max_size= 10):
        self.max_size = max_size
        self.cola = []
        self.direccion = 1
        
    def insertar(self, elemento):
        if len(self.cola) < self.max_size:
            self.cola.append(elemento)

        else: 
            if  self.direccion == 1:
                self.cola.pop(0)
                self.cola.append(elemento)

            else:
                self.cola.pop()
                self.cola.insert(0, elemento)

            if  len(self.cola) == self.max_size:
                self.direccion *=  -1
    def estado(self):
         return ''.join(self.cola)

Cola_Especial = ColaEspecial()

secuencia = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letra in secuencia:
    Cola_Especial.insertar(letra)

print("El estado final de la secuencia es el siguiente:", Cola_Especial.estado()) 