1# This program creates a DataFrame with student scores in different subjects, calculates the correlation matrix, and displays both the DataFrame and the correlation matrix.
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

2# This program creates a simple line plot using Matplotlib to visualize the relationship between two sets of data points.
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create line plot
plt.plot(x, y, linestyle='--', color='r', marker='o', label='Data line')

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

# Add legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

3# This program demonstrates how to create a histogram and a box plot using Matplotlib to visualize the distribution of a dataset.
import matplotlib.pyplot as plt

# Data
data = [22, 87, 5, 43, 56, 13, 55, 54, 20, 51, 5]

# Histogram
plt.hist(data, bins=5, color='purple', label='Histogram Data')
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Box plot
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

4# This program creates a pie chart using Matplotlib to visualize the distribution of different categories in a dataset.
import matplotlib.pyplot as plt
import numpy as np

# Pie chart data
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # explode the 2nd slice

# Pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures pie is circular
plt.show()

