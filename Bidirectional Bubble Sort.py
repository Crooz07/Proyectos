def bidirectionalBubbleSort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        # Bubble largest element to the right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        right -= 1

        # Bubble smallest element to the left
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

        left += 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bidirectionalBubbleSort(arr)
print("Sorted array is:", arr)
