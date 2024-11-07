def insertionSortAndDedupe(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        if arr[j + 1] != key:  # Only insert if it's not a duplicate
            arr[j + 1] = key

    # Remove the duplicates by slicing the array
    return list(dict.fromkeys(arr))

# Example usage
arr = [4, 5, 4, 3, 2, 2, 1]
print("Sorted and deduplicated array:", insertionSortAndDedupe(arr))