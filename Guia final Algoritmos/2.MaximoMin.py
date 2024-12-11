def maximo_minimo(arr):
    maximo = arr[0]
    minimo = arr[0]
    for num in arr:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    return maximo, minimo


print("Máximo y Mínimo:", maximo_minimo([3, 1, 4, 1, 5]))
