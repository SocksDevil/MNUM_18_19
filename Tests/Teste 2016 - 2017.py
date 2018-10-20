import math
def math_func_Ex_1(x):
    return (0.662*x - 1)/(x-1)
def bissect(a, b, func, error):
    while(abs(a - b) > error):
        m = (a+b)/2
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m


#print(bissect(1.1, 2, math_func_Ex_1, 10**(-5)))

def math_func_x(x,y):
    return 1 - pow(x, 2) - y
def math_func_dev_x(x,y):
    return 1 - 2*x
def math_func_y(x,y):
    return 0.7 + x- y
def math_func_dev_y(x,y):
    return -1


def newton_linear(x, y, func_x, func_dev_x, func_y, func_dev_y, error):
    prev_x = 0
    prev_y = 0
    while(abs(x-prev_x) > error) and (abs(y-prev_y) > error):
        prev_x = x
        prev_y = y
        x = prev_x - func_x(prev_x, prev_y)/func_dev_x(prev_x, prev_y)
        y = prev_y - func_y(prev_x, prev_y)/func_dev_y(prev_x, prev_y)
    return x, y

#print(newton_linear(-1, -1, math_func_x, math_func_dev_x, math_func_y, math_func_dev_y, 10**(-3)))