import math
def func_x(x, y, z, t):
    return (1 + y + z -t)/4.5   

def func_y(x, y, z, t):
    return (-1 + x - z + t)/4.5

def func_z(x, y, z, t):
     return (-1 + x - 2*y + t)/4.5

def func_t(x, y, z, t):
    return (-2*x + y + z)/4.5




def gauss_jacobi(x, y, z, t, func_x, func_y, func_z, func_t):
    prev_x, prev_y, prev_z, prev_t = 0,0,0,0
    for _ in range(0, 2):
        prev_x, prev_y, prev_z, prev_t = x, y, z, t
        x = func_x(prev_x, prev_y, prev_z,prev_t)
        y = func_y(prev_x, prev_y, prev_z,prev_t)
        z = func_z(prev_x, prev_y, prev_z,prev_t)
        t = func_t(prev_x, prev_y, prev_z,prev_t)
        print(x, y, z, t)

gauss_jacobi(0.25, 0.25, 0.25, 0.25, func_x, func_y, func_z, func_t)

#Exercise 3 c

def exercise_4(t, T):
    return -0.25 * (T - 45)

def euler(t, T, a, b, h, func):
    n = int(abs(a-b)/h)
    for _ in range(0, n):
        T = T + h * func(t, T)
        t = t + h
    return t, T

# print(euler(1, 23, 1, 1.8, 0.4, exercise_4))