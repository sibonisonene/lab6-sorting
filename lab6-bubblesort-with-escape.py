import time
import matplotlib.pyplot as plt

# Bubble sort function with an escape clause
def bubble_sort_with_escape(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Escape clause: track if a swap occurred
        
        # Inner loop to perform the swaps
        for j in range(0, n - 1 - i):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True  # A swap occurred
        
        # If no swap happened, the list is already sorted
        if not swapped:
            break
    
    return arr

# Function to test performance of bubble sort on best-case situations
def test_bubble_sort_best_case_performance():
    sizes = [1, 5, 10, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]  # Different list sizes
    results = []
    
    for size in sizes:
        # Generate a sorted list for the best case
        arr = list(range(size))  # Best case: already sorted
        
        # Time the sorting process
        start_time = time.time()
        bubble_sort_with_escape(arr)
        end_time = time.time()
        
        # Record the time taken
        duration = end_time - start_time
        results.append((size, duration))
    
    return results

# Function to test performance of bubble sort on worst-case situations
def test_bubble_sort_worst_case_performance():
    sizes = [1, 5, 10, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]  # Different list sizes
    results = []
    
    for size in sizes:
        # Generate a reversed list for the worst case
        arr = list(range(size, 0, -1))  # Worst case: reverse sorted
        
        # Time the sorting process
        start_time = time.time()
        bubble_sort_with_escape(arr)
        end_time = time.time()
        
        # Record the time taken
        duration = end_time - start_time
        results.append((size, duration))
    
    return results

# Run the performance tests
best_case_results = test_bubble_sort_best_case_performance()
worst_case_results = test_bubble_sort_worst_case_performance()

# Extract list sizes and corresponding times
best_sizes = [size for size, duration in best_case_results]
best_times = [duration for size, duration in best_case_results]

worst_sizes = [size for size, duration in worst_case_results]
worst_times = [duration for size, duration in worst_case_results]

# Plot the graphs
plt.figure(figsize=(12, 6))

# Best Case
plt.subplot(1, 2, 1)
plt.plot(best_sizes, best_times, marker='o', color='green', label='Best Case (O(n))')
plt.title('Best Case Performance of Bubble Sort')
plt.xlabel('List Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()

# Worst Case
plt.subplot(1, 2, 2)
plt.plot(worst_sizes, worst_times, marker='o', color='red', label='Worst Case (O(n^2))')
plt.title('Worst Case Performance of Bubble Sort')
plt.xlabel('List Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
