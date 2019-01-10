import math

def exercise_1(t):
    return -0.25*(t - 37)

def euler(t, T, h, func):
    for _ in range(0, 2):
        T = T + h * func(T)
        t+=h
    return T

# print(euler(5, 3, 0.4, exercise_1))

def exercise_4(x):
    return 2 * math.log(2 * x)


def picard_peano(x, func):
    for _ in range(0, 2):
        print(x)
        x = func(x)

# picard_peano(1.1, exercise_4)

def exercise_5(x):
    return math.sqrt(1 + 2.5 * 2.5 * math.exp(5*x))


def trapezium(a, b, h, func):
    n = int(abs(b - a)/h)
    values = []
    for i in range(1, n):
        values.append(2 * func(a + i * h))
    integral = func(a) + func(b)

    for i in values:
        integral+=i

    integral*=h/2
    return integral

def simpson(a, b, h, func):
    n = int(abs(b - a)/h)
    values = []
    for i in range(1, n, 2):
        values.append(4 * func(a + i * h))
    
    for i in range(2, n, 2):
        values.append(2 * func(a + i * h))
    integral = func(a) + func(b)

    for i in values:
        integral+=i

    integral*=h/3
    
    return integral


# print(trapezium(0, 1, 0.125, exercise_5))
# print(simpson(0, 1, 0.125, exercise_5))
# print(trapezium(0, 1, 0.125/2, exercise_5))
# print(simpson(0, 1, 0.125/2, exercise_5))
# print(trapezium(0, 1, 0.125/4, exercise_5))
# print(simpson(0, 1, 0.125/4, exercise_5))

def exercise_7(x):
    return pow(x, 3) - 10 * math.sin(x) + 2.8

def bissection(a, b, func, error):
    m = 0
    counter = 0
    while abs(a - b) > error and counter < 2:
        counter+=1
        m = (a + b)/2
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m

print(bissection(1.5, 4.2, exercise_7, 10**(-5)))