import math
def math_question_5(x):
    return pow(x,3) + 2 * pow(x, 2) + 10 * x - 17

def math_question_5_dev(x):
    return 3 * pow(x, 2) + 4 * x + 10

def newton(x, func, func_dev, error):
    prev_x = 50
    while abs(x-prev_x) > error:
        prev_x = x
        print(x)
        x = x - func(x)/func_dev(x)
    return x

# print(newton(0, math_question_5, math_question_5_dev, 10**(-5)))

def math_func_y(x, y):
    return y - math.log(x - 1, math.e)

def math_func_dev_y(x,y):
    return 1

def math_func_x(x,y):
    return pow(y, 2) + pow(x-3, 2) - 4

def math_func_dev_x(x,y):
    return 2 * (x-3)

def newton_equations(x, y, func_x, func_dev_x, func_y, func_dev_y, error):
    prev_x = 0
    prev_y = 0
    print(x,y)
    while (abs(x - prev_x) > error) or (abs(y - prev_y) > error):
        prev_x = x
        prev_y = y
        x = prev_x -  (func_x(x,y)/func_dev_x(prev_x,prev_y))
        y = prev_y -  (func_y(x,y)/func_dev_y(prev_x, prev_y))
        print(x, y)
    return x, y

print(newton_equations(1.5, 1.3, math_func_x, math_func_dev_x, math_func_y, math_func_dev_y, 10**(-5)))

# The newton algorithm is well implemented, yet the algorithm is still failing