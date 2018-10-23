import math
def math_ex_3(x):
    return math.exp(x) - pow(x, 2) + 3*x - 2
def math_ex_dev_3(x):
    return math.exp(x) - 2 * x + 3

def newton(x, func, func_dev, error):
    counter = 0
    prev_x= 500
    while abs(prev_x - x) > error:
        prev_x = x
        x = prev_x - func(prev_x)/func_dev(prev_x)
        counter+=1
    return (x , counter)

# print(newton(0.1, math_ex_3, math_ex_dev_3, 10**(-4)))

def math_ex_4(x):
    return pow(x, 2) - x - 1.2

def bissection(a, b, func, error):
    counter = 0
    m = 0
    while abs(a - b) > error:
        counter+=1
        m = (a + b)/2
        if (func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m, counter

# print(bissection(1 , 2, math_ex_4, 10**(-7)))

def math_ex_5(x):
    return 3 * x + math.sin(x) - math.exp(x)

def rope(a, b, func, error):
    counter = 0
    m = 0
    while abs(a - b) > error:
        counter+=1
        m = (a * func(b) - b * func(a))/(func(b) - func(a))
        if (func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m, counter

# print(rope(0, 1, math_ex_5, 10**(-5)))

# g(x) = x^2 - 0.2
def math_ex_6(x):
    return pow(x, 2) - 0.2

def math_ex_dev_6(x):
    return 2 * x

def picard_peano(x, func, func_dev, error):
    if(func_dev(x) >= 1):
        return "Function does not converge"
    prev_x = 500
    while abs(x - prev_x) > error:
        prev_x = x
        x = func(prev_x)
    return x

print(picard_peano(0, math_ex_6, math_ex_dev_6, 10**(-7)))
    