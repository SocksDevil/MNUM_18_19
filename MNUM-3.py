import math

def func(x):
    return math.sin(x)

def trapezium_rules(a, b,n, func):
    area = 0
    h = (b-a)/n
    values = []
    for i in range(0, n):
        values.append(func(a+i*h))
    for i in values:
        area+=i

    area*=2
    area += func(a)
    area += func(b)
    area*=h/2
    return area

print(trapezium_rules(0, math.pi,12,func))
