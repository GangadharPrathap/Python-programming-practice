import numpy as np
import time
# Task 1
temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

average_f = np.mean(temps_fahrenheit)
print("Average Fahrenheit:", round(average_f, 1))


# Task 2
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)  # or scores.shape[0]
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
print("Range:", np.max(scores) - np.min(scores))


# Task 3
n = 50000
np_array = np.arange(1, n + 1)
py_list = list(range(1, n + 1))

start_np = time.time()
sum_np = np.sum(np_array)
end_np = time.time()

start_py = time.time()
sum_py = sum(py_list)
end_py = time.time()

time_np = end_np - start_np
time_py = end_py - start_py

print("NumPy sum:", int(sum_np))
print("Python sum:", int(sum_py))
print(f"NumPy time: {time_np:.4f} seconds")
print(f"Python time: {time_py:.4f} seconds")

if sum_np != sum_py:
    print("Warning: sums do not match!")

if time_np > 0:
    faster = time_py / time_np
    print(f"NumPy is {faster:.1f}x faster")
else:
    print("NumPy time too small to measure accurately.")