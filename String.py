import string


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def is_palindrome(input_string):
    # Limpiamos la cadena: eliminamos espacios, puntuación y ponemos todo en minúsculas
    cleaned_string = ''.join(char.lower()
                             for char in input_string if char.isalpha())

    stack = Stack()

    # Insertamos cada letra de la cadena limpia en la pila
    for char in cleaned_string:
        stack.push(char)

    # Reconstruimos la cadena usando la pila (para invertirla)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    # Comparamos la cadena limpia con su versión invertida
    return cleaned_string == reversed_string


# Programa de prueba
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" es un palíndromo.')
else:
    print(f'"{test_string}" no es un palíndromo.')
