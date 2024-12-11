def parentesis_balanceados(cadena):
    pila = []
    for char in cadena:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila:
                return False
            top = pila.pop()
            if (char == ")" and top != "(") or \
               (char == "}" and top != "{") or \
               (char == "]" and top != "["):
                return False
    return len(pila) == 0


print("Paréntesis Balanceados:", parentesis_balanceados("({[]})"))
