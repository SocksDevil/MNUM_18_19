import math

def concentration(t, C, T):
   return -math.exp(-0.1/(T+273)) * C

def temperature(t, C, T):
    return 15 * math.exp(-0.1/(T+273)) * C - 0.1*(T - 20)

def euler(t, C, T, a, b, h, func_C, func_T):
    n = int(abs(b-a)/h)
    for i in range(0, n):
        prev_C , prev_T = C, T
        C = C + h * func_C(t, prev_C, prev_T)
        T = T + h * func_T(t, prev_C, prev_T)
        t = t + h
    return t, C, T

# print(euler(0.5, 2, 20, 0.5, 1, 0.25, concentration, temperature))
# print(euler(0.5, 2, 20, 0.5, 1, 0.25/2, concentration, temperature))
# print(euler(0.5, 2, 20, 0.5, 1, 0.25/4, concentration, temperature))

# QC = 2.247208574502132
# erro = 0.007021341253097428


def rk4(t, C, T, a, b, h, func_C, func_T):
    n = int(abs(b-a)/h)
    for i in range(0, n):
        dC1 = h * func_C(t, C, T)
        dT1 = h * func_T(t, C, T)

        dC2 = h * func_C(t + h/2, C + dC1/2, T + dT1/2)
        dT2 = h * func_T(t + h/2, C + dC1/2, T + dT1/2)

        dC3 = h * func_C(t + h/2, C + dC2/2, T + dT2/2)
        dT3 = h * func_T(t + h/2, C + dC2/2, T + dT2 /2 )

        dC4 = h * func_C(t + h, C + dC3, T + dT3)
        dT4 = h * func_T(t + h, C + dC3, T + dC3)

        t = t + h
        C = C + 1/6*dC1 + 1/3*dC2 + 1/3*dC3 + 1/6*dC4
        T = T + 1/6 * dT1 + 1/3 * dT2 + 1/3 * dT3 + 1/6 * dT4
    return t, C, T

# print(rk4(0.5, 2, 20, 0.5, 1, 0.25, concentration, temperature))
def exercise_4(t,T):
    return -0.25*(T - 64)

def euler_4(t, T, a, b, h, func):
    n = int(abs(b-a)/h)
    for i in range(0, n):
        T = T + h * func(t, T)
        t = t + h
        print(t, T)
    
# euler_4(4, 0, 4, 5, 0.5, exercise_4)

def func_x(x,y ,z , t):
    return (25 - 0.5*y - 3*z - 0.25*t)/6

def func_y(x,y ,z , t):
    return (10 - 1.2*x - 0.25*z - 0.2*t)/3

def func_z(x,y ,z , t):
    return (7 - 0.25*y - -1*x - 2*t)/4

def func_t(x,y ,z , t):
    return (-12 - 4*y - z - 2*x)/8

    
def gauss_seidel(x, y , z , t, func_x, func_y, func_z, func_t):

    for i in range(0, 1):
        x = func_x(x, y, z, t)
        y = func_y(x, y, z, t)
        z = func_z(x, y, z, t)
        t = func_t(x, y, z, t)
        print(x, y, z, t)

# gauss_seidel(2.83865, 2.22131, 4.17630, -3.84236, func_x, func_y, func_z, func_t)