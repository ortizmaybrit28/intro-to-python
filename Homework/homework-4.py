# Question 1: DEBUGGING
'''
Asks that we comment on how we debugged
the question (if error is encountered.)
'''


# Question 2.1: MAKING A LIST VARIABLE
whateverNameYouWant = list(range(21))
print(whateverNameYouWant)
'''
No problems encountered with this line of code
for question 2 part 1
'''


# Question 2.2: WORKING WITH LIST ELEMENTS
whateverNameYouWant = list(range(21))
def squareList(input_list):
	return [x ** 2 for x in input_list]
anotherNameYouWant = squareList(whateverNameYouWant)
print(anotherNameYouWant)
'''
I encountered the following error: SyntaxError: invalid syntax
This was caused by a spelling error and spacing in the 
anotherNameYouWant, so I went ahead fixed the error and spacing.
'''


# Question 2.3: SLICING
whateverNameYouWant = list(range(21))  
def squareList(input_list):
    return [x ** 2 for x in input_list]
anotherNameYouWant = squareList(whateverNameYouWant)
def first_fifteen_elements(input_list):
    return input_list[:15]
result = first_fifteen_elements(anotherNameYouWant)
print(result)
'''
I encountered the following error: NameError: name 'first_fifth_element' 
is not defined. So I went ahead a fixed the formatting and spelling error,
as I spelt the list wrong, instead of fifteen, I wrote five.
'''


# Question 2.4: STRIDING
whateverNameYouWant = list(range(21))
def squareList(input_list):
    return [x ** 2 for x in input_list]
anotherNameYouWant = squareList(whateverNameYouWant)
def every_fifth_elements(input_list):
    return input_list[4::5]
result = every_fifth_elements(anotherNameYouWant)
print(result)
'''
I am getting a list with every multiple of 5, not the fifth elements
from the respective list. I believe my input_list[::5] is incorrect.
I went ahead and did [4::5], where start from index 4 and extract every
fifth element from the list.
'''


# Question 2.5: SLICING & STRIDING
whateverNameYouWant = list(range(21))
def squareList(input_list):
    return [x ** 2 for x in input_list]
anotherNameYouWant = squareList(whateverNameYouWant)
def fancy_function(input_list):
    last_30 = input_list[-30:]
    return last_30[::-3]
result = fancy_function(anotherNameYouWant)
print(result)
'''
No issues encountered! :D
'''


# Question 3.1: CREATING A 5x5 2D LIST
def create_2d_list():
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(i * 5 + j + 1)
        matrix.append(row)
    return matrix
matrix = create_2d_list()
for row in matrix:
    print(row)
'''
No issues encountered!Just took a while to come up :)
'''


# Question 3.2: REPLACING 2D LIST WITH MULTIPLES OF 3
def modified_2d_list(matrix):
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):  
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
matrix = create_2d_list()
modified_matrix = modified_2d_list(matrix)
for row in modified_matrix:
    print(row)
'''
Only concern was that the modulus would get the incorrect element
so I went ahead and added that it absolutely equals 0 (== 0)
'''


# Question 3.3: SUMMING NONE-'?' ELEMENTS
def sum_non_question_elements(matrix):
    total = 0
    for row in matrix:
        for element in row: 
            if element != "?":
                total += element
    return total
matrix = create_2d_list()
new_matrix = modified_2d_list(matrix)
result = sum_non_question_elements(new_matrix)
print(result)
'''
No errors encountered!
'''


