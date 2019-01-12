import math


def picard_peano(x, func):
    print(func(x))

# picard_peano(0.9, lambda x: 2 * math.log(2*x))

# def exercise_3(t, x):
#     return math.sin(x) + math.sin(2 * t)

def rk4(t, x, h, a, b, func):
    n = int(abs(b - a)/h)
    for _ in range(0, n):
        d1 = h * func(t, x)
        d2 = h * func(t + h/2, x + d1/2)
        d3 = h * func(t + h/2, x + d2/2)
        d4 = h * func(t + h, x + d3)
        x = x + d1/6 + d2/3 + d3/3 + d4/6
        t += h
    print(t, x)


rk4(1, 0, 0.5, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
rk4(1, 0, 0.5/2, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
rk4(1, 0, 0.5/4, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
rk4(1, 0, 0.5/8, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
rk4(1, 0, 0.5/16, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
rk4(1, 0, 0.5/32, 1, 1.5, lambda t, x: math.sin(x) + math.sin(2 * t))
