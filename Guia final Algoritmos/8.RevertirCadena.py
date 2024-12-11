def revertir_cadena(cadena):
    pila = []
    for char in cadena:
        pila.append(char)
    resultado = ""
    while pila:
        resultado += pila.pop()
    return resultado


print("Revertir Cadena:", revertir_cadena("Hola"))
