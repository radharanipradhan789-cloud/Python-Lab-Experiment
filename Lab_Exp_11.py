1# This program demonstrates the use of NumPy for creating and manipulating arrays, including indexing and slicing operations.
import numpy as np

print("=== Part 1: ndarray, Indexing, and Slicing ===")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)

# Accessing elements
print("Element at (0,1):", arr[0,1])   # first row, second column
print("Row 1:", arr[1])                # second row
print("Column 2:", arr[:,2])           # third column


2# This program demonstrates the properties and functions of NumPy arrays, including creating arrays of ones, zeros, and empty arrays, as well as examining the shape, size, and number of dimensions of a 2D array.
import numpy as np

# Experiment 11 - Part 3: Array Properties and Functions
print("=== Part 3: Array Properties and Functions ===")

# Ones array
ones_arr = np.ones((2,3))
print("Ones Array:\n", ones_arr)

# Zeros array
zeros_arr = np.zeros((2,5))
print("Zeros Array:\n", zeros_arr)

# Empty array
empty_arr = np.empty((2,3))
print("Empty Array:\n", empty_arr)

# Example 2D array
arr = np.array([[1,2,3],[4,5,6]])
print("Example 2D Array:\n", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Number of Dimensions:", arr.ndim)

3# This program demonstrates various statistical operations on a NumPy array, including finding the maximum, minimum, sum, and product of the elements. It also shows how to use broadcasting to perform element-wise operations on the array.
import numpy as np

# Create array
arr = np.array([1, 2, 3])
print("Array:", arr)

# Statistical operations
print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Product:", arr.prod())

# Broadcasting example
print("Broadcast result (arr + 5):", arr + 5)

4# This program demonstrates how to save and load NumPy arrays using the np.save and np.load functions. It creates a NumPy array, saves it to a file, and then loads it back into memory, printing the loaded array to the console.
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4])

# Save array to file
np.save('my_array.npy', arr)

# Load array from file
loaded_arr = np.load('my_array.npy')
print("Loaded array:", loaded_arr)

5# This program demonstrates how to create a Pandas Series, which is a one-dimensional labeled array capable of holding any data type. The program initializes a Series with a list of data and corresponding labels, and then prints the Series to the console.
import pandas as pd

# Create a pandas series
data = [10, 20, 30]
labels = ['a', 'b', 'c']

series = pd.Series(data, index=labels)
print("Pandas Series:\n", series)

6# This program demonstrates how to create a DataFrame using the Pandas library, display the entire DataFrame, access specific columns and rows, and print the results.
import pandas as pd

# Create a dictionary with data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the entire DataFrame
print("DataFrame:")
print(df)

# Display the 'Age' column
print("\nIn Age column:")
print(df['Age'])

# Display the row at index 1
print("\nRow at index 1:")
print(df.iloc[1])

7# This program creates a DataFrame with student scores in different subjects, calculates the correlation matrix, and displays both the DataFrame and the correlation matrix.
import pandas as pd

# Create a dictionary with data
data = {
    'Math': [90, 85, 80, 95],
    'Science': [68, 82, 85, 90],
    'English': [78, 75, 80, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Data Frame:")
print(df)

# Calculate correlation matrix
correlation = df.corr()

# Display correlation matrix
print("\nCorrelation Matrix:")
print(correlation)