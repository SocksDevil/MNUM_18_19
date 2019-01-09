import math

def exercise_1_g(x):
    return pow(4*pow(x,3) - x + 1, 1/4)

def picard_peano(x, func):
    for _ in range(0, 2):
        print(x)
        x = func(x)
    print(x)

# picard_peano(4, exercise_1_g)

def exercise_6(x):
    return x + pow(x-2, 2)/(math.sin(x) + 4)

def aurea(x1, x2, func, error):
    B = (math.sqrt(5) - 1)/2
    A = B * B
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        print(x1, x2, x3, x4, func(x1), func(x2), func(x3), func(x4))
        if(func(x3) < func(x4)):
            x2 = x4
        else:
            x1 = x3
        

# aurea(-1, 1.5, exercise_6, 10**(-5))

def exercise_7(x):
    return -x + 60 * math.cos(math.sqrt(x)) + 2

def exercise_7_dev(x):
    return - (30 * math.sin(math.sqrt(x))/math.sqrt(x)) - 1

def newton(x, func, func_dev):
    for _ in range(0, 3):
        print(x, func(x))
        x = x - func(x)/func_dev(x)

newton(1.8, exercise_7, exercise_7_dev)
