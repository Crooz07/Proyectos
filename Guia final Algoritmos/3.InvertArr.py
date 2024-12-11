def invertir_arreglo(arr):
    invertido = []
    for i in range(len(arr) - 1, -1, -1):
        invertido.append(arr[i])
    return invertido


print("Invertir un Arreglo:", invertir_arreglo([1, 2, 3, 4]))
