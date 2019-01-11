import math

def exercise_1_y(x, y):
    return -y + pow(x, 2) - 1.2

def exercise_1_x(x,y):
    return  -x + pow(y, 2) - 1

def exercise_1_x_dev_y(x, y):
    return 2 * y

def exercise_1_x_dev_x(x, y):
    return -1

def exercise_1_y_dev_y(x, y):
    return -1

def exercise_1_y_dev_x(x, y):
    return 2 * x


def newton(x, y, fx, fx_x, fx_y, fy, fy_x, fy_y, error):
    prev_x, prev_y = 0, 0
    for _ in range(0, 2):
        prev_x, prev_y = x, y
        print(x, y)
        x = prev_x - (fx(prev_x, prev_y) * fy_y(prev_x, prev_y) - fy(prev_x, prev_y) * fx_y(prev_x, prev_y))/(fx_x(prev_x, prev_y)*fy_y(prev_x, prev_y) - fy_x(prev_x, prev_y)*fx_y(prev_x, prev_y)) 
        y = prev_y - (fy(prev_x, prev_y) * fx_x(prev_x, prev_y) - fx(prev_x, prev_y) * fy_x(prev_x, prev_y))/(fx_x(prev_x, prev_y)*fy_y(prev_x, prev_y) - fy_x(prev_x, prev_y)*fx_y(prev_x, prev_y))
    return x, y

# print(newton(1, 1, exercise_1_y, exercise_1_y_dev_x, exercise_1_y_dev_y, exercise_1_x, exercise_1_x_dev_x, exercise_1_x_dev_y, 10**(-5)))

def exercise_4(x):
    return pow(x, 7) + 0.5 * x - 0.5

def rope(a, b, func, error):
    w = 0
    while abs(a - b) > error:
        w = (a * func(b) - b * func(a))/(func(b) - func(a))
        print(a, b, w)
        if(func(a) * func(w) < 0 ):
            b = w
        else:
            a = w
    return w

# rope(0, 0.8, exercise_4, 10**(-5))

def exercise_5_y(t, x, y):
    return x

def exercise_5_z(t, x, y):
    return 0.5 + pow(t, 2) + t * x

def euler(t, y, z, h, func_y, func_z):
    for _ in range(0, 2):
        prev_y, prev_z = y, z
        y = y + h * func_y(t, prev_z, prev_y)
        z = z + h * func_z(t, prev_z, prev_y)
        t+=h
        print(t, y, z)

# euler(0, 0, 1, 0.25, exercise_5_y, exercise_5_z)

def rk4(t, y, z, h, func_y, func_z):
    for _ in range(0, 2):
        d1_y = h * func_y(t, z, y)
        d1_z = h * func_z(t, z, y)

        d2_y = h * func_y(t + h/2, z + d1_z/2, y + d1_y/2)
        d2_z = h * func_z(t + h/2, z + d1_z/2, y + d1_y/2)

        d3_y = h * func_y(t + h/2, z + d2_z/2, y + d2_y/2)
        d3_z = h * func_z(t + h/2, z + d2_z/2, y + d2_y/2)

        d4_y = h * func_y(t + h, z + d3_z, y + d3_y)
        d4_z = h * func_z(t + h, z + d3_z, y + d3_y)

        y = y + 1/6 * d1_y + 1/3 * d2_y + 1/3 * d3_y + 1/6 * d4_y
        z = z + 1/6 * d1_z + 1/3 * d2_z + 1/3 * d3_z + 1/6 * d4_z

        t+=h
        
        print(t, y, z)
        
# rk4(0, 0, 1, 0.25, exercise_5_y, exercise_5_z)


def exercise_6(x):
    return math.sqrt(1 +  1.5 * 1.5 * math.exp(3 * x))

def trapezium(a, b, h, func):
    n = int(abs(b - a)/h)
    values = []
    integral = func(a) + func(b)

    for i in range(1, n):
        values.append(2 * func(a + i * h))
    
    for i in values:
        integral+=i
    
    integral*=h/2
    return integral


def simpson(a, b, h, func):
    n = int(abs(b - a)/h)
    values = []
    integral = func(a) + func(b)

    for i in range(1, n, 2):
        values.append(4 * func(a + i * h))

    for i in range(2, n, 2):
        values.append(2 * func(a + i * h))
    
    for i in values:
        integral+=i
    
    integral*=h/3
    return integral

# print(trapezium(0, 2, 0.5, exercise_6))
# print(trapezium(0, 2, 0.5/2, exercise_6))
# print(trapezium(0, 2, 0.5/4, exercise_6))
# print(simpson(0, 2, 0.5, exercise_6))
# print(simpson(0, 2, 0.5/2, exercise_6))
# print(simpson(0, 2, 0.5/4, exercise_6))
