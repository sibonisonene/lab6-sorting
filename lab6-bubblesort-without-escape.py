import time
import random
import matplotlib.pyplot as plt

# Bubble sort function with no escape clause
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to test performance of bubble sort on lists of different sizes
def test_bubble_sort_performance():
    sizes = [1, 5, 10, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]  # Different list sizes
    results = []
    
    for size in sizes:
        # Generate a random list of the given size
        arr = [random.randint(0, size) for _ in range(size)]
        
        # Time the sorting process
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        
        # Record the time taken
        duration = end_time - start_time
        results.append((size, duration))
    
    return results

# Run the performance test
performance_results = test_bubble_sort_performance()

# Extract list sizes and corresponding times
sizes = [size for size, duration in performance_results]
times = [duration for size, duration in performance_results]

# Plot the graph
plt.plot(sizes, times, marker='o')
plt.title('Bubble Sort Performance (No Escape Clause)')
plt.xlabel('List Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()

