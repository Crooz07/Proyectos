class Array:
    def __init__(self, arr):
        self.arr = sorted(arr)  # Ensure the array is sorted

    def median(self):
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
        else:
            return self.arr[n // 2]

# Example usage
array = Array([12, 3, 5, 7, 19])
print("Median is:", array.median())