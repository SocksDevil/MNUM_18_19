import math

#[3.2 , 3.3]
#[5.5, 5.7]

def math_ex_1(x):
    return math.sin(10 * x) + math.cos(3*x)

def math_ex_dev_1(x):
    return 10 * math.cos(10 * x) - math.sin(3 * x) * 3

def bissection(a, b, func, relative_error):
    m = 0
    counter  = 0
    while (abs(a - b)/a) > relative_error:
        m = (a + b)/2
        counter+=1
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m, counter


# print(bissection(3.2, 3.3, math_ex_1, 0.005))
# print(bissection(5.5, 5.7, math_ex_1, 0.005))

def rope(a, b, func, relative_error):
    m = 0
    counter  = 0
    while (abs(a - b)/a) > relative_error:
        m = (a * func(b) - b * func(a))/(func(b) - func(a))
        counter+=1
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m, counter


# print(rope(3.1, 3.3, math_ex_1, 0.005))
# print(rope(5.5, 5.7, math_ex_1, 0.005))

def newton(x, func, func_dev, relative_error):
    prev_x = 0
    counter = 0
    while abs(x - prev_x)/x > relative_error:
        prev_x = x
        counter+=1
        x = prev_x - func(prev_x)/func_dev(prev_x)

    return x, counter

# print(newton(3.2, math_ex_1, math_ex_dev_1, 0.005))
# print(newton(5.6, math_ex_1, math_ex_dev_1, 0.005))

#Exercise 2
# x = e^(-x)
# x = - ln(x)

def math_ex_2(x):
    return math.exp(-x)

def math_ex_dev_2(x):
    return -math.exp(-x)

def picard_peano(x, func, func_dev, error):
    prev_x = 0
    if(func_dev(x) >= 1):
        return "Function does not converge"
    while abs(prev_x - x) > error:
        prev_x = x
        x = func(prev_x)
    return x

# print(picard_peano(-0.5, math_ex_2, math_ex_dev_2, 10**(-5)))


def math_f1(x,y):
    return x + y - 3

def math_f1_x(x, y):
    return 1

def math_f1_y(x, y):
    return 1

def math_f2(x, y):
    return pow(x, 2) + pow(y, 2) - 9

def math_f2_x(x, y):
    return 2 * x

def math_f2_y(x, y):
    return 2 * y

def newton_equations(x, y, f1, f1_x, f1_y, f2, f2_x, f2_y, error):
    prev_x = 0
    prev_y = 0
    while (abs(prev_x - x)/x > error) or (abs(prev_y - y)/y > error):
        prev_x = x
        prev_y = y
        denom = f1_x(prev_x, prev_y)*f2_y(prev_x, prev_y) - f2_x(prev_x, prev_y)*f1_y(prev_x, prev_y)
        x = prev_x - (f1(prev_x, prev_y)*f2_y(prev_x, prev_y) - f2(prev_x, prev_y)*f1_y(prev_x, prev_y))/denom
        y = prev_y - (f2(prev_x, prev_y)*f1_x(prev_x, prev_y) - f1(prev_x, prev_y)*f2_x(prev_x, prev_y))/denom
    return x, y

print(newton_equations(4, 1, math_f1, math_f1_x, math_f1_y, math_f2, math_f2_x, math_f2_y, 0.005))