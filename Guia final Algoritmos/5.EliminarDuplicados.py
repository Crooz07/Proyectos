def eliminar_duplicados(arr):
    resultado = []
    for num in arr:
        if num not in resultado:
            resultado.append(num)
    return resultado


print("Eliminar Duplicados:", eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))
