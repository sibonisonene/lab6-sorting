import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to test performance of Merge Sort
def test_merge_sort_performance():
    sizes = [1, 5, 10, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]  # Different list sizes
    times = []

    for size in sizes:
        # Generate a random list of the given size
        arr = [random.randint(0, 100000) for _ in range(size)]

        # Measure the time taken to sort the array
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()

        # Record the time taken
        duration = end_time - start_time
        times.append(duration)

    return sizes, times

# Run the performance test
sizes, times = test_merge_sort_performance()

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, times, marker='o', color='blue', label='Merge Sort Performance')
plt.title('Merge Sort Performance Test')
plt.xlabel('List Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
