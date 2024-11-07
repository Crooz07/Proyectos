def insertionSortWithCount(arr):
    comparisons = 0
    copies = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            copies += 1
            j -= 1
        arr[j + 1] = key
        copies += 1
        comparisons += 1
    print(f"Comparisons: {comparisons}, Copies: {copies}")

# Example usage
arr = [12, 11, 13, 5, 6]
insertionSortWithCount(arr)
print("Sorted array is:", arr)