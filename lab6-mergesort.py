import time
import matplotlib.pyplot as plt

# Merge Sort function
def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize indices for merging
        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to test performance of merge sort
def test_merge_sort_performance():
    sizes = [1, 5, 10, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]  # Different list sizes
    results = []

    for size in sizes:
        # Generate a random list of the given size
        arr = [i for i in range(size)]  # For best case: already sorted
        # arr = [size - i for i in range(size)]  # For worst case: reverse sorted
        
        # Time the sorting process
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        
        # Record the time taken
        duration = end_time - start_time
        results.append((size, duration))
    
    return results

# Run the performance tests
merge_sort_results = test_merge_sort_performance()

# Extract list sizes and corresponding times
sizes = [size for size, duration in merge_sort_results]
times = [duration for size, duration in merge_sort_results]

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(sizes, times, marker='o', color='blue', label='Merge Sort Performance')
plt.title('Performance of Merge Sort')
plt.xlabel('List Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
