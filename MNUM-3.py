import math
import matplotlib.pyplot as plt

def func(x):
    return math.sin(x)

def trapezium_rules(a, b, n, func):
    area = 0
    h = (b-a)/n
    values = []
    for i in range(1, n):
        values.append(func(a+i*h))
    for i in values:
        area+=i

    area*=2
    area += func(a)
    area += func(b)
    area*=h/2
    return area

# print(trapezium_rules(0, math.pi,12,func))
# print(trapezium_rules(math.pi/4, math.pi, 50,func))

def simpson(a, b, n, func):
    area = 0
    n *=2
    h = (b-a)/n
    values= []

    for i in range(1,n, 2):
        values.append(func(a+i*h)*4)

    for i in range(2,n, 2):
        values.append(func(a+i*h)*2)

    area+=func(a)
    area+=func(b)

    for i in values:
        area+=i

    area*=h/3
    return area

# print(simpson(0, math.pi,6, func))


def error_calculator(area, real_area):
    return abs(area-real_area)

def multiple_errors(a, b, rule, func):
    errors = []
    errors.append(error_calculator(rule(a, b, 2, func),2))
    errors.append(error_calculator(rule(a, b, 4, func),2))
    errors.append(error_calculator(rule(a, b, 8, func),2))
    errors.append(error_calculator(rule(a, b, 10, func),2))
    errors.append(error_calculator(rule(a, b, 20, func),2))
    errors.append(error_calculator(rule(a, b, 40, func),2))

    n = []
    n.append(2)
    n.append(4)
    n.append(8)
    n.append(10)
    n.append(20)
    n.append(40)
    return n, errors

# print(multiple_errors(0, math.pi, trapezium_rules, func))
# print(multiple_errors(0, math.pi, simpson, func))

def plot(a, b, rule, func):
    n, errors = multiple_errors(a , b, rule, func)
    plt.plot(n, errors, '-')
    plt.show()



plot(0,math.pi, trapezium_rules, func)
plot(0, math.pi, simpson, func)