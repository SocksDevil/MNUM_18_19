import math

def func_x(x, y, z, t):
    return (1 + y + z - t)/4.8
    
def func_y(x, y, z, t):
    return (-1 + x - z + t)/4.8

def func_z(x, y, z, t):
    return (-1 + x - 2*y +t )/4.8

def func_t(x, y, z, t):
    return (-2*x + y + z)/4.8


def gauss_seidel(x, y, z, t, func_x, func_y, func_z, func_t):
    for i in range(0, 2):
        x = func_x(x, y, z, t)
        y = func_y(x, y, z, t)
        z = func_z(x, y, z, t)
        t = func_t(x, y, z, t)
        print(x, y, z, t)


# gauss_seidel(0, 0, 0, 0, func_x, func_y, func_z, func_t)

def exercise_4(v, u):
    return u * (u/2 + 1) * pow(v, 3) + (u + 5/2) * pow(v, 2)

def euler(u, v, a, b, h, func):
    n  = int(abs(b-a)/h)
    for i in range(0, n):
        v = v + h * func(v, u)
        u = u + h
    return u, v


print(euler(1, 0.1, 1, 1.8, 0.08, exercise_4))
print(euler(1, 0.1, 1, 1.8, 0.08/2, exercise_4))
print(euler(1, 0.1, 1, 1.8, 0.08/4, exercise_4))