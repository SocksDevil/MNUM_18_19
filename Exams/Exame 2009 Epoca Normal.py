import math

def newton(x, func, func_dev):
    for _ in range(0, 1):
        x = x - func(x)/func_dev(x)
    print(x)

# newton(1.8, lambda x: x - 2.6 + pow(math.cos(x + 1.1), 3), lambda x: 1 - 3 * pow(math.cos(x + 1.1), 2)*math.sin(x + 1.1))

def aurea(x1, x2, func):
    B = (math.sqrt(5) - 1)/2
    A = B * B
    for _ in range(0, 3):
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        print(x1, x2, x3, x4, func(x1), func(x2), func(x3), func(x4))
        if(func(x3) < func(x4)):
            x2 = x4
        else:
            x1 = x3
    print(x2 - x1)

# aurea(2, 4, lambda x: 5 * math.cos(x) - math.sin(x))


def rk4(t, x, a, b, h, func):
    n = int(abs(b -a)/h)
    for _ in range(0, n):
        d1 = h * func(t, x)
        d2 = h * func(t + h/2, x + d1/2)
        d3 = h * func(t + h/2, x + d2/2)
        d4 = h * func(t + h, x + d3)
        x = x + 1/6 * d1 + 1/3 * d2 + 1/3 * d3 + 1/6 * d4
        t += h
        print(t, x)

    print("1.5 Value: ", x)

# rk4(1, 1, 1, 1.5, 0.5, lambda t, x: math.sin(x) + math.sin(2 * t))
# rk4(1, 1, 1, 1.5, 0.5/2, lambda t, x: math.sin(x) + math.sin(2 * t))
# rk4(1, 1, 1, 1.5, 0.5/4, lambda t, x: math.sin(x) + math.sin(2 * t))
    