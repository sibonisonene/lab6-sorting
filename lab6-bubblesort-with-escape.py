def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Initialize swapped as False at the start of each pass
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the elements are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Mark that a swap has occurred
        # If no elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_optimized(arr)
print("Sorted array:", arr)
