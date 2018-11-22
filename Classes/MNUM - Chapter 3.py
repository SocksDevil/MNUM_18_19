import math

def gaussian_elimination_3x3(matrix, results):
    if(matrix[0][0] != 1):
        for i in matrix[0]:
            i /= matrix[0][0]
        results[0] /= matrix[0][0]
    for i in range(0, 3):
        matrix[1][i]+= matrix[0][i] * -matrix[1][0]
    results[1] += results[0] * -matrix[1][0]

    if(matrix[1][1] != 1):
        for i in matrix[1]:
            i /= matrix[1][1]
        results[1] /= matrix[1][1]
    for i in range(0, 3):
        matrix[2][i]+= matrix[1][i] * -matrix[2][1]
    results[2] += results[1] * -matrix[2][1]
    z = results[2]/matrix[2][2]
    y = results[1] - (z * matrix[1][2])
    x = results[0] - (z * matrix[0][2] + y * matrix[0][1])
    return x, y, z

matrix = [[3, -1, 2], [1, 1, 1], [2, 0, 1]]
results = [-1, 8, 5]

# print(gaussian_elimination_3x3(matrix, results))

def func1(x2,x3):
    return (7 - x2 -x3)/3

def func2(x1,x3):
    return (4-x1-2*x3)/4

def func3(x1,x2):
    return (5-2*x2)/5

def gauss_jacobi(x1, x2, x3, func1, func2, func3, error):
    prev_x1 = 500
    prev_x2 = 500
    prev_x3 = 500
    while (abs(func1(x2, x3) - func1(prev_x2, prev_x3)) > error or abs(func2(x1, x3) - func2(prev_x1, prev_x3)) > error or abs(func3(x1,x2) - func3(prev_x1, prev_x2)) > error):
        prev_x1 = x1
        prev_x2 = x2
        prev_x3 = x3
        x1 = func1(prev_x2,prev_x3)
        x2 = func2(prev_x1, prev_x3)
        x3 = func3(prev_x1, prev_x2)
    return x1, x2, x3

def gauss_seidel(x1, x2, x3, func1, func2, func3, error):
    prev_x1 = 500
    prev_x2 = 500
    prev_x3 = 500
    while (abs(func1(x2, x3) - func1(prev_x2, prev_x3)) > error or abs(func2(x1, x3) - func2(prev_x1, prev_x3)) > error or abs(func3(x1,x2) - func3(prev_x1, prev_x2)) > error):
        prev_x1 = x1
        prev_x2 = x2
        prev_x3 = x3
        x1 = func1(x2,x3)
        x2 = func2(x1, x3)
        x3 = func3(x1, x2)
    return x1, x2, x3

    

print(gauss_jacobi(0, 0, 0, func1, func2, func3, 10**(-5)))
print(gauss_seidel(0, 0, 0, func1, func2, func3, 10**(-5)))