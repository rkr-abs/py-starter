import numpy as np


data = [1, 2, 3, 4, 5]
# Create a 1-dimensional NumPy array from a Python list
array = np.array(data)

# Perform some operations with NumPy array
print("Original array:", array)
print("Sum of elements:", np.sum(array))
print("Mean of elements:", np.mean(array))
print("Maximum element:", np.max(array))
print("Minimum element:", np.min(array))
print("Square root of elements:", np.sqrt(array))
print("Element-wise multiplication by 2:", array * 2)

# Create a 2-dimensional NumPy array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform operations with 2-dimensional array
print("\nOriginal matrix:")
print(matrix)

print("Transpose of matrix:")
print(matrix.T)

print("Sum of rows:")
print(np.sum(matrix, axis=1))

print("Sum of columns:")
print(np.sum(matrix, axis=0))
