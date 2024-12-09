# Question 1: THE ODD ONES OUT
import numpy as np
def onlyOdd(arr):
    odd_rows = arr[np.all(arr % 2 != 0, axis=1)]
    return odd_rows
arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
result = onlyOdd(arr)
print(result)


# Question 2.1
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    return matrix
matrix = checkerboard()
print(matrix)


# Question 2.2
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    for i in range(0, 7, 2):
        matrix[i, ::2] = 1
        matrix[i, 1::2] = 0
    return matrix
matrix = checkerboard()
print(matrix)


# Question 2.3
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    for i in range(1, 8, 2):  
        matrix[i, ::2] = 0  
        matrix[i, 1::2] = 1  
    for i in range(0, 8, 2):  
        matrix[i, ::2] = 1 
        matrix[i, 1::2] = 0  
    return matrix
matrix = checkerboard()
print(matrix)


# Question 2.4
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    for i in range(1, 8, 2):  
        matrix[i, ::2] = 1  
        matrix[i, 1::2] = 0  
    for i in range(0, 8, 2):  
        matrix[i, ::2] = 0 
        matrix[i, 1::2] = 1  
    return matrix
matrix = checkerboard()
print(matrix)


# Question 3: THE EXPANDING UNIVERSE
import numpy as np
def expansion(universe, num_spaces):
    expanded_list = []
    for word in universe:
        if num_spaces == 1:
            expanded_word = ' '.join(word) 
        elif num_spaces == 2:
            expanded_word = '  '.join(word)
        expanded_list.append(expanded_word)
    return np.array(expanded_list)

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))
print(expansion(universe, 2))


# Question 4
import numpy as np
def secondLargest(planets):
    sorted_columns = np.sort(planets, axis=0)
    second_largest = sorted_columns[-2, :]
    return second_largest
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
result = secondLargest(planets)
print(planets)
print(result)



