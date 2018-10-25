import math

def math_ex_4(x):
    return math.exp(1.5 * x)

def simpson(a, b, h, func):
    n = int(abs(b-a)/h)
    values = []
    integral = 0
    for i in range(1, n, 2):
        values.append(func(a + i * h) * 4)
    for i in range(2, n, 2):
        values.append(func(a + i * h) * 2)
    for i in values:
        integral+=i
    integral+= func(a) + func(b)
    integral*=h/3
    return integral

# print(simpson(1 , 1.5, 0.125/4, math_ex_4))

def math_ex_5(x):
    return x - 3.7 + pow(math.cos(x + 1.2), 3)

def math_ex_dev_5(x):
    return 1 - 3 * pow(math.cos(x + 1.2), 2)*math.sin(x + 1.2)

def newton_first_iter(x, func, func_dev, error):
    return (x - func(x)/func_dev(x))

print(newton_first_iter(3.8, math_ex_5, math_ex_dev_5, 10**(-5)))