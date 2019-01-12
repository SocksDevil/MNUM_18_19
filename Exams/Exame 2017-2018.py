import math


def aurea(x1, x2, func, error):
    B = (math.sqrt(5) - 1)/2
    A = B * B
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if(func(x3) < func(x4)):
            x2 = x4
        else:
            x1 = x3
    return x1, x2

print(aurea(-2, 2, lambda x: pow(x - 4, 2) + pow(x, 4), 10**(-5)))

def exercise_2(x):
    return math.sqrt(1 + 2.5 * 2.5 * math.exp(5 * x))

def trapezium(a, b, h, func):
    n = int(abs(b - a)/h)
    integral = func(a) + func(b)
    values = []

    for i in range(1, n):
        values.append(2 * func(a + i * h))
    
    for i in values:
        integral+= i
    
    integral*= h/2

    return integral


def simpson(a, b, h, func):
    n = int(abs(b - a)/h)  
    integral = func(a) + func(b)
    values = []

    for i in range(1, n, 2):
        values.append(4 * func(a + i * h))

    for i in range(2, n, 2):
        values.append(2 * func(a + i * h))

    for i in values:
        integral+= i
    
    integral*= h/3

    return integral


# print(trapezium(0, 1, 0.125, exercise_1))
# print(trapezium(0, 1, 0.125/2, exercise_1))
# print(trapezium(0, 1, 0.125/4, exercise_1))
# print(simpson(0, 1, 0.125, exercise_1))
# print(simpson(0, 1, 0.125/2, exercise_1))
# print(simpson(0, 1, 0.125/4, exercise_1))

def exercise_4_C(t, C, T):
    return - math.exp(-0.5/(T + 273)) * C

def exercise_4_T(t, C, T):
    return 30 * math.exp(-0.5/(T + 273)) * C - 0.5 * (T - 20)

def euler(t, C, T, h,a, b, func_C, func_T):
    n = int(abs(b-a)/h)
    for _ in range(0, n):
        prev_C, prev_T = C, T

        C = prev_C + h * func_C(t, prev_C, prev_T)
        T = prev_T + h * func_T(t, prev_C, prev_T)
        t+= h
        
    print(t, C, T)

def rk4(t, C, T, h, func_C, func_T):
    for _ in range(0, 2):
        dC1 = h * func_C(t, C, T)
        dT1 = h * func_T(t, C, T)

        dC2 = h * func_C(t + h/2, C + dC1/2, T + dT1/2)
        dT2 = h * func_T(t + h/2, C + dC1/2, T + dT1/2)

        dC3 = h * func_C(t + h/2, C + dC2/2, T + dT2/2)
        dT3 = h * func_T(t + h/2, C + dC2/2, T + dT2/2)

        dC4 = h * func_C(t + h, C + dC3, T + dT3)
        dT4 = h * func_T(t + h, C + dC3, T + dT3)

        C = C + 1/6 * dC1 + 1/3 * dC2 + 1/3 * dC3 + 1/6 * dC4
        T = T + 1/6 * dT1 + 1/3 * dT2 + 1/3 * dT3 + 1/6 * dT4
        t+= h
        print(t, C, T)


# euler(0, 2.5, 25, 0.25,0, 0.5, exercise_4_C, exercise_4_T)
# euler(0, 2.5, 25, 0.25/2,0, 0.5, exercise_4_C, exercise_4_T)
# euler(0, 2.5, 25, 0.25/4,0, 0.5, exercise_4_C, exercise_4_T)
# rk4(0, 2.5, 25, 0.25, exercise_4_C, exercise_4_T)

def exercise_5(x, y):
    return -1.1 * x * y + 12 * y + 7 * pow(x, 2) - 8 * x

def exercise_5_dev_x(x, y):
    return -1.1 * y + 14 * x - 8

def exercise_5_dev_y(x, y):
    return -1.1 * x + 12

def gradient(x, y, h, gradient, func, error):
    xn, yn = 0, 0
    flag = False
    for _ in range(0, 2):
        if(flag):
            x, y = xn, yn

        xn = x - h * gradient[0](x, y)
        yn = y - h * gradient[1](x, y)
        if(func(xn, yn) < func(x, y)):
            h*=2
            flag = True
        else:
            h/=2
            flag = False
    print(func(x, y))

gradient(3, 1, 0.1,[exercise_5_dev_x, exercise_5_dev_y], exercise_5, 10**(-3))
