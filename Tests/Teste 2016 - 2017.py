import math
def math_func_Ex_1(x):
    return (0.662*x - 1)/(x-1)
def bissect(a, b, func, erro):
    while(abs(a - b) > erro):
        m = (a+b)/2
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m


print(bissect(1.1, 2, math_func_Ex_1, 10**(-5)))