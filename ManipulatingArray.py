import numpy as np
array = np.random.randint(0, 10, size=(5,5), dtype=int)
print(array)
#if you count starting with 0 it goes 2nd row, 3rd column, but if you start at 1 it is 3rd row, 4th column
print("The number from the 2nd row, 3rd column is", array[2,3])
print("The sum of all the elements in the array is", np.sum(array))
print("The mean of each row in the array is", np.mean(array, axis=1))
print("The maximum value in each column of the array is", np.max(array, axis=0))
#numpy is really short/ simple and is honestly really easy to pull an output from an array
