import math
def math_ex_4(x):
    return 2 * math.log(2*x)

def picard_peano(x, func, error):
    prev_x = 0
    while abs(x - prev_x) > error:
        prev_x = x
        print(x)
        x = func(x)
    return x
# print(picard_peano(1.1, math_ex_4, 10**(-5)))

def math_ex_5(x):
    return math.sqrt(1 + pow(2.5*math.exp(2.5*x), 2))

def trapezium(a, b, h, func):
    n = int(abs(b-a)/h)
    values = []
    integral = 0
    for i in range(1, n):
        values.append(func(a + i * h))
    for i in values:
        integral+=2*i
    integral+= func(a)+func(b)
    integral*=h/2
    return integral

# print(trapezium(0, 1, 0.125/4, math_ex_5))


def simpson(a, b, h, func):
    n = int(abs(b-a)/h)
    integral = 0
    values = []

    for i in range(1, n, 2):
        values.append(func(a + i* h)*4)

    for i in range(2 , n, 2):
        values.append(func(a + i * h)*2)

    for i in values:
        integral+=i
    integral+= func(a) + func(b)
    integral*=h/3
    return integral

# print(simpson(0 , 1, 0.125/4, math_ex_5))

def math_ex_7(x):
    return pow(x, 3) - 10 * math.sin(x) + 2.8

def bissection(a, b , func, error):
    m = 0
    while abs(a - b) > error:
        m = (a+b)/2
        print(m)
        if (func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m

# bissection(1.5, 4.2, math_ex_7, 10**(-5))

def temperature(t, T):
    return -0.25*(T - 37)

def euler(t, T, h, n, func):
    for _ in range(0, n):
        T = T + h * func(t, T)
        t = t + h
    return t, T

print(euler(5, 3, 0.4, 2, temperature))

#  Exercise 3
# for i:1 thru 3 do(
# A : rowop(A, i, i, 1 - 1/A[i][i]),
#     for j:1 thru 3 do(
#     if(i # j) then A : rowop(A, j, i, A[j][i])
#     )
# );