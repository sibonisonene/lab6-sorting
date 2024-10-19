import time
import random
def bubble_sort(arr):
    n = len(arr)
    # Perform n-1 passes over the array
    for i in range(n):
        # Compare each pair of adjacent elements
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the elements are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
