def pila_calculadora(operaciones):
    pila = []
    for item in operaciones:
        if isinstance(item, int):
            pila.append(item)
        else:
            b = pila.pop()
            a = pila.pop()
            if item == "+":
                pila.append(a + b)
            elif item == "-":
                pila.append(a - b)
            elif item == "*":
                pila.append(a * b)
            elif item == "/":
                pila.append(a // b)
    return pila.pop()


print("Pila Calculadora:", pila_calculadora([3, 4, "+", 2, "*"]))
