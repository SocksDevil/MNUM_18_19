import math
def math_func(x):
    return (x - 2*math.log(x, math.exp(1))-5)

def math_func_dev(x):
    return (1- 2/x)

def math_g_func(x):
    return (2*math.log(x, math.exp(1))+5)

def math_g_sec_func(x):
    return math.exp((x-5)/2)

def math_g_sec_func_dev(x):
    return math.exp((x-5)/2)/2

def math_g_func_dev(x):
    return 2/x


#Using maxima it was determined the function had 2 zeros

# # 1st zero [0.01, 1]
# print(math_func(0.01))
# print(math_func(1))
#
# # 2st zero [9, 10]
# print(math_func(9))
# print(math_func(10))

def bissect(a, b, erro, func):
    m = 0
    while abs(a-b) > erro:
        m = (a+b)/2
        if(func(a)*func(m) < 0):
            b = m
        else:
            a = m
    return m

#print(bissect(0.01, 1, 10**(-5), math_func))

def rope(a, b, error, func):
    m = 0
    while abs(a-b) > error:
        m = (func(b)*a-b*func(a))/(func(b)-func(a))

        if (func(a)*func(m) < 0):
            b = m
        else:
            a = m
    
    return m

#print(rope(0.01, 1, 10**(-5), math_func))

def tangent(a, error, func, func_dev):
    prev_x = 0
    while abs(a-prev_x) > error:
        prev_x = a
        a = a - (func(a))/func_dev(a)
    return a

#print(tangent(9, 10**(-5), math_func, math_func_dev))

def picard_peano(a, error, func, func_dev):
    prev_x = 0
    if func_dev(a) >= 1:
        return "Impossible to solve with this method"
    while abs(a - prev_x) > error:
        prev_x = a
        a = func(a)
    return a

#print(picard_peano(9, 10**(-5), math_g_func, math_g_func_dev))

def sin(x):
    return math.sin(x)

def trapezium(a, b, n, func):
    h = (a+b)/n
    values = []
    area = 0
    for i in range(1, n):
        values.append(func(a+i*h))
    values*=2
    for i in values:
        area+=i
    area+=func(a) + func(b)
    area*=h/2
    return area

#print(trapezium(0,math.pi, 12, sin))

def simpson(a, b, n, func):
    n*=2
    h = (a+b)/n
    values = []
    area = 0
    for i in range(1, n, 2):
        values.append(func(a+i*h)*4)

    for i in range(2, n, 2):
        values.append(func(a+i*h)*2)

    for i in values:
        area+=i
    area+=func(a) + func(b)
    area*=h/3
    return area

#print(simpson(0, math.pi, 6, sin))


def math_2_var_func(x, y):
    return x*y

# x = [4 , 12]
# y = [3, 8]
def simpson_cube_aux(row, h, func):
    integral = 0
    for j in range(2 , len(row), 2):
        row[j]*=2
    for j in range(1 , len(row), 2):
        row[j]*=4
    for i in row:
        integral+=i
    integral+= row[0] + row[len(row) - 1]
    integral*=h/3
    return integral

def simpson_cube(x0, x, y0, y, n, func):
    hX = (abs(x0 - x))/n
    hY = (abs(y0 - y))/n
    squares = []
    row = []
    for i in range(0, n):
        row.clear()
        for j in range(0 , n):
            row.append(func(x0 + i*hX, y0 + j*hY))
        squares.append(simpson_cube_aux(row, hY, func))
    return(simpson_cube_aux(squares, hX, func))

print(simpson_cube(4, 12, 3, 8, 6, math_2_var_func))

    
        
        
        