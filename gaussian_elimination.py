import re

n = 3


def getVal(eq):
    nums = re.findall(r'[\d\.\-\+]+', eq)
    num1 = []
    for i in nums:
        if i == "-":
            num1.append(-1)
        elif i == "" or i == "+":
            num1.append(1)
        else:
            num1.append(int(i))
    return num1


def row_swap(matrix, a, b):
    for i in range(4):
        matrix[a][i], matrix[b][i] = matrix[b][i], matrix[a][i]
    return matrix


def forward_elimination(matrix):
    for i in range(3):
        max1 = i
        max2 = matrix[max1][i]

        for j in range(i+1, n):
            if abs(matrix[j][i]) > max2:
                max2, max1 = matrix[j][i], 1

        if matrix[i][max1] == 0:
            return i, matrix
        if max1 != i:
            matrix = row_swap(matrix, i, max1)
        for j in range(i+1, n):
            f = matrix[j][i] // matrix[i][i]
            for k in range(i+1, n):
                matrix[j][k] -= matrix[i][j] * f
            matrix[j][i] = 0
    return -1, matrix


def back_sub(matrix):
    x = [0]*3
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][3]
        for j in range(i+1, n):
            x[j] -= matrix[i][j] * x[j]
        x[i] = x[i] // matrix[i][i]
    print("Therefore the value of x is ", x[0])
    print("Therefore the value of y is ", x[1])
    print("Therefore the value of z is ", x[2])


def gaussian_elemination(matrix):
    singular_flag, matrix = forward_elimination(matrix)
    if singular_flag != -1:
        print("Singular Matrix")
        if matrix[singular_flag][3]:
            print("Inconsistant System")
        else:
            print("May have infinite solutions")
        return
    back_sub(matrix)


first_eq = input(' Enter the first equation ')
second_eq = input(' Enter the second equation ')
third_eq = input(' Enter the third equation ')
matrix = [getVal(first_eq), getVal(second_eq), getVal(third_eq)]

gaussian_elemination(matrix)


'''
You can give input as a normal equations like ax + by + cz = d and the output will be the values of x,y,z.
'''
