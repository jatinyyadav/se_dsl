#JATIN YADAV
#COMP-B
#7226

import sys

def input_matrix():
    matrix=[]
    row=int(input("Enter the number of rows: "))
    column=int(input("Enter the number of columns: "))
    for i in range(row):
        x=[]
        for j in range(column):
            element = int(input(f"Enter element {i},{j}: "))
            x.append(element)
        matrix.append(x)
    return matrix    

def isUpperTriangular(matrix):
    row = len(matrix)
    for i in range(1, row):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
    return True

def add_matrix(matrix1, matrix2):
    result = []
    row = len(matrix1)
    col = len(matrix1[0])
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(matrix1[i][j] + matrix2[i][j])
        result.append(temp)
    return result

def subtract_matrix(matrix1, matrix2):
    result = []
    row = len(matrix1)
    col = len(matrix1[0])
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(matrix1[i][j] - matrix2[i][j])
        result.append(temp)
    return result

def primary_diagonal_sum(matrix):
    ans = 0
    row = len(matrix)
    for i in range(row):
        ans += matrix[i][i]
    return ans

def secondary_diagonal_sum(matrix):
    ans = 0
    row = len(matrix)
    for i in range(row):
        ans += matrix[i][row - 1 - i]
    return ans

def multiply(matrix1, matrix2):
    r1 = len(matrix1)
    c1 = len(matrix1[0])
    r2 = len(matrix2)
    c2 = len(matrix2[0])
    
    result = [[0]*c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def saddle_point(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    for i in range(row):
        min_in_row = min(matrix[i])
        col_index = matrix[i].index(min_in_row)
        
        is_saddle_point = True
        for j in range(row):
            if matrix[j][col_index] > min_in_row:
                is_saddle_point = False
                break
        
        if is_saddle_point:
            return min_in_row, (i, col_index)
    
    return "No saddle point"

def switch_case(response, matrix1, matrix2):
    switcher = {
        1: lambda: isUpperTriangular(matrix1),
        2: lambda: add_matrix(matrix1, matrix2),
        3: lambda: subtract_matrix(matrix1, matrix2),
        4: lambda: primary_diagonal_sum(matrix1),
        5: lambda: secondary_diagonal_sum(matrix1),
        6: lambda: multiply(matrix1, matrix2),
        7: lambda: saddle_point(matrix1)
    }
    
    func = switcher.get(response, lambda: "Invalid choice")
    return func()

# Input matrices
matrix_1 = input_matrix()
matrix_2 = input_matrix()

ans = True

while ans:
    response = int(input(f"--------------------MENU--------------------\n1. Checking upper triangular\n2. Addition\n3. Subtraction\n4. Primary diagonal sum\n5. Secondary diagonal sum\n6. Multiplication\n7. Saddle point\n8. Exit\nEnter your choice: "))
    
    if response == 8:
        ans = False
    else:
        result = switch_case(response, matrix1=matrix_1, matrix2=matrix_2)
        print(result)
