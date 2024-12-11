def buscar_elemento(arr, elemento):
    for num in arr:
        if num == elemento:
            return True
    return False


print("Buscar un Elemento:", buscar_elemento([1, 2, 3, 4], 3))
