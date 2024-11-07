class Array:
    def __init__(self, arr):
        self.arr = sorted(arr)

    def deduplicate(self):
        deduped_arr = []
        for i in range(len(self.arr)):
            if i == 0 or self.arr[i] != self.arr[i - 1]:
                deduped_arr.append(self.arr[i])
        return deduped_arr

# Example usage
array = Array([1, 1, 2, 3, 4, 4, 5])
print("Deduplicated array:", array.deduplicate())