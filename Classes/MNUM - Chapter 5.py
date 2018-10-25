import math

def math_function(x, y):
    return pow(x, 2) + pow(y, 2)

def euler_first_order(x, y, a, b, h, func):
    n = int(abs(b-a)/h)
    for i in range(0, n+1):
        y = y + h * math_function(x, y)
        x = x + h
    return y

# print(euler_first_order(0, 0, 0, 1.4, 0.1, math_function))

def rk_second_order(x, y, a, b, h, func):
    n = int(abs(b-a)/h)
    for i in range(0, n+1):
        y = y + h * func(x + h/2, y+h/2*func(x,y))
        x = x + h
    return y

# print(rk_second_order(0, 0, 0, 1.4, 0.1, math_function))


def rk_fourth_order(x, y, a, b, h, func):
    n = int(abs(b-a)/h)
    for i in range(0, n+1):
        delta_1 = h * func(x, y)
        delta_2 = h * func(x+h/2, y + delta_1/2)
        delta_3 = h * func(x + h/2, y + delta_2/2)
        delta_4 = h * func(x+ h, y + delta_3)
        y = y + delta_1/6 + delta_2/3 + delta_3/3 + delta_4/6
        x = x + h
    return y


# print(rk_fourth_order(0, 0, 0, 1.4, 0.1, math_function))

def calculate_qc_and_error(x, y, a, b, h, denom, func, method):
    s = method(x, y, a, b, h, func)
    s_line = method(x, y, a, b, h/2, func)
    s_double_line = method(x, y, a, b, h/4, func)
    qc = (s_line - s)/(s_double_line - s_line)
    error = (s_double_line - s_line)/denom
    return qc, error

print(calculate_qc_and_error(0, 0, 0, 1.4, 0.1, 1, math_function, euler_first_order))
print(calculate_qc_and_error(0, 0, 0, 1.4, 0.1, 3, math_function, rk_second_order))
print(calculate_qc_and_error(0, 0, 0, 1.4, 0.1, 15, math_function, rk_fourth_order))