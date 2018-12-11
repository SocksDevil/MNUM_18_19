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
    for _ in range(0, 2):
        prev_x, prev_y, prev_z, prev_t = x, y, z, t
        x = func_x(prev_x, prev_y, prev_z, prev_t)
        y = func_y(prev_x, prev_y, prev_z, prev_t)
        z = func_z(prev_x, prev_y, prev_z, prev_t)
        t = func_t(prev_x, prev_y, prev_z, prev_t)
        print(x, y, z, t)

# gauss_jacobi(0.25, 0.25, 0.25, 0.25, func_x, func_y, func_z, func_t)

def exercise_2(t, x):
        return math.sin(2 *x) + math.sin(2 * t)

def rk4(t, x, a, b, h, func):
        n = int(abs(b-a)/h)
        for _ in range(0, n):
                delta1 = h * func(t, x)
                delta2 = h * func(t + h/2, x + delta1/2)
                delta3 = h * func(t + h/2, x + delta2/2)
                delta4 = h * func(t + h, x + delta3)
                x = x + delta1/6 + delta2/3 + delta3/3 + delta4/6
                t = t + h
                print(t, x)
# print("h = 0.5")     
# rk4(1, 1, 1, 1.5, 0.5, exercise_2)
# print("h = 0.25")     
# rk4(1, 1, 1, 1.5, 0.5/2, exercise_2)
# print("h = 0.125")     
# rk4(1, 1, 1, 1.5, 0.5/4, exercise_2)


def concentration(t, C, T):
        return -math.exp(-0.5/(T + 273))*C

def temperature(t, C, T):
        return 20 * math.exp(-0.5/(T + 273))*C - 0.5 * (T - 20)

def euler(t, C, T, h, func_C, func_T):
        for _ in range(0, 2):
                prev_C, prev_T = C, T
                T = T + h * func_T(t, prev_C, prev_T)
                C = C + h * func_C(t, prev_C, prev_T)
                print(t, C, T)

def rk4(t, C, T, h, func_C, func_T):
        for _ in range(0, 2):
                d1_C = h * func_C(t, C, T)
                d1_T = h * func_T(t, C, T)

                d2_C = h * func_C(t + h/2, C + d1_C/2, T + d1_T/2)
                d2_T = h * func_T(t + h/2, C + d1_C/2, T + d1_T/2)

                d3_C = h * func_C(t + h/2, C + d2_C/2, T + d2_T/2)
                d3_T = h * func_T(t + h/2, C + d2_C/2, T + d2_T/2)

                d4_C = h * func_C(t + h, C + d3_C,T + d3_T)
                d4_T = h * func_T(t + h, C + d3_C,T + d3_T)
                T = T + d1_T/6 + d2_T/3 + d3_T/3 + d4_T/6
                C = C + d1_C/6 + d2_C/3 + d3_C/3 + d4_C/6
                print(t, C, T)

# rk4(0, 2, 20, 0.2, concentration, temperature)
# euler(0, 2, 20, 0.2, concentration, temperature)