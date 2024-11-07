def oddEvenSort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        # Odd phase
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        # Even phase
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

# Example usage
arr = [34, 2, 10, -9]
oddEvenSort(arr)
print("Sorted array is:", arr)