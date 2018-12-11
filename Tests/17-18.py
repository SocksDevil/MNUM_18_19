import math

def func_x(x, y, z, t):
    return (25 - 0.5 *y - 3*z - 0.25*t)/6


def func_y(x, y, z, t):
    return (10 - 1.2 *x - 0.25*z - 0.2*t)/3


def func_z(x, y, z, t):
    return (7 + x - 0.25*y - 2*t)/4


def func_t(x, y, z, t):
    return (-12 - 2*x - 4*y - z)/8


def gauss_seidel(x, y, z, t, func_x, func_y, func_z, func_t):
    for _ in range(0, 1):
        x = func_x(x, y, z, t)
        y = func_y(x, y, z, t)
        z = func_z(x, y, z, t)
        t = func_t(x, y, z, t)
        print(x, y, z, t)

# gauss_seidel(2.12687, 2.39858, 3.99517, -3.73040, func_x, func_y, func_z, func_t)

def func_dev_y(t, y, z):
        return z

def func_dev_z(t, y, z):
        return 2 + pow(t, 2) + t*z

def euler(t, y, z, a, b, h, func_dev_y, func_dev_z):
        for _ in range(0, 2):
                prev_y, prev_z = y, z
                y = y + h * func_dev_y(t, y, z)
                z = z + h * func_dev_z(t, y, z)
                t = t + h
                print(t, y, z)

# euler(1, 1, 0, 1, 1.5, 0.25, func_dev_y, func_dev_z)

def rk4(t, y, z, a, b, h, func_dev_y, func_dev_z):
        for _ in range(0, 2):
                d1_y = h * func_dev_y(t, y, z)
                d1_z = h * func_dev_z(t, y, z)

                d2_y = h * func_dev_y(t + h/2, y + d1_y/2,z + d1_z/2)
                d2_z = h * func_dev_z(t + h/2, y + d1_y/2,z + d1_z/2)              

                d3_y = h * func_dev_y(t + h/2, y + d2_y/2,z + d2_z/2)
                d3_z = h * func_dev_z(t + h/2, y + d2_y/2,z + d2_z/2)

                d4_y = h * func_dev_y(t + h, y + d3_y, z + d3_z)
                d4_z = h * func_dev_z(t + h, y + d3_y, z + d3_z)

                y = y + d1_y/6 + d2_y/3 + d3_y/3 + d4_y/6
                z = z + d1_z/6 + d2_z/3 + d3_z/3 + d4_z/6
                t = t + h
                print(t, y, z)

rk4(1, 1, 0, 1, 1.5, 0.25, func_dev_y, func_dev_z)