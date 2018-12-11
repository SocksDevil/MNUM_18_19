#################### Pergunta 1 ######################
# 1. O uso de nuúmeros do tipo inteiro permite que a divisão dos intervalos seja feita de uma forma 
# prevenindo qualquer problema para a divisão. No entanto, o uso de inteiros impede que haja um controlo
# preciso, uma vez que o step entre iterações será relativamente elevado, gerando erros elevados.
# 2. O uso de floats, aumenta de facto a precisão do valor obtido no cálculo. No entanto, a utlização
# de um valor do tipo float, poderá criar um problema de arredondamento, de modo a que o valor alcançado
# poderá ja ultrapassar o falor desejado.
# 3. O uso da combinação de floats traz significativas melhorias ao processo de controlo do
# alcançe do valor desejado uma vez que poderá se usar um step (h) controlado, dividido corretamente
# entre intervalos determinados pelo inteiro i.
# 4. O uso do expoente poderá ser uma metodologia semelhante à anterior que conseguirá de uma forma 
# precisa chegar ao valor desejado, sem o ultrapassar
import math

def math_func_f(x,y):
     return pow(x, 2) - y - 1.2

def math_func_f_x(x, y):
    return 2*x
def math_func_f_y(x,y):
    return -1

def math_func_g(x, y):
    return -x + pow(y, 2) - 1
def math_func_g_x(x,y):
    return -1

def math_func_g_y(x,y):
    return 2*y

def newton_equations(x, y, f, f_x, f_y, g, g_x, g_y, error):
    prev_x = 0
    prev_y = 0
    while (abs(x - prev_x) > error) or (abs(y - prev_y) > error):
        prev_x = x
        prev_y = y
        print(x, y)
        x = prev_x -  (f(prev_x, prev_y)*g_y(prev_x, prev_y) - g(prev_x, prev_y)*f_y(x,y))/(f_x(prev_x, prev_y)*g_y(prev_x, prev_y) - g_x(prev_x, prev_y)*f_y(prev_x, prev_y))
        y = prev_y -  (g(prev_x, prev_y)*f_x(prev_x, prev_y) - f(prev_x, prev_y)*g_x(x,y))/(f_x(prev_x, prev_y)*g_y(prev_x, prev_y) - g_x(prev_x, prev_y)*f_y(prev_x, prev_y))
    return x, y

# print(newton_equations(1, 1, math_func_f, math_func_f_x, math_func_f_y, math_func_g, math_func_g_x, math_func_g_y, 10**(-5)))

def math_ex_4(x):
    return pow(x, 7) + 0.5*x - 0.5

def rope(a, b, func, error):
    m = 0
    while abs(a - b) > error:
        m = (a*func(b) - b * func(a))/(func(b)- func(a))
        print(a, b, m)
        if(func(a) * func(m) < 0):
            b = m
        else:
            a = m
    return m

# print(rope(0, 0.8, math_ex_4, 10**(-5)))
def math_ex_6(x):
    return math.sqrt(1 + pow(1.5*math.exp(1.5*x), 2))
def trapezium(a, b, h, func):
    n = int(abs(b - a)/h)
    values = []
    for i in range(1, n):
        values.append(func(a + i * h))
    integral = 0
    for i in values:
        integral+=2*i
    integral+=func(a) + func(b)
    integral*=h/2
    return integral

# print(trapezium(0, 2, 0.125, math_ex_6))

def simpson(a, b, h, func):
    n = int(abs(b-a)/h)
    values = []
    for i in range(1, n, 2):
        values.append(4 * func(a + i * h))
        
    for i in range(2, n, 2):
        values.append(2 * func(a + i * h))
    integral = 0
    for i in values:
        integral+=i
    integral+=func(a) + func(b)
    integral*=h/3
    return integral
# print(simpson(0, 2, 0.125, math_ex_6))


def func_y(t, y, z):
    return z

def func_z(t, y, z):
    return (0.5 + t * t + t*z)

def euler(t, y, z, h, func_y, func_z):
    for _ in range(0,2):
        prev_y, prev_z = y, z
        y = y + h * func_y(t, prev_y, prev_z)
        z = z + h * func_z(t, prev_y, prev_z)
        t = t + h
        print(t, y, z)

def rk4(t, y, z, h, func_y, func_z):
    for _ in range(0, 2):
        d1_y = h * func_y(t, y, z)
        d1_z = h * func_z(t, y, z)

        d2_y = h * func_y(t + h/2, y + d1_y/2, z + d1_z/2)
        d2_z = h * func_z(t + h/2, y + d1_y/2, z + d1_z/2)

        d3_y = h * func_y(t + h/2, y + d2_y/2, z + d2_z/2)
        d3_z = h * func_z(t + h/2, y + d2_y/2, z + d2_z/2)

        d4_y = h * func_y(t + h, y + d3_y, z + d3_z)
        d4_z = h * func_z(t + h, y + d3_y, z + d3_z)
        
        t = t + h
        y = y + d1_y/6 + d2_y/3 + d3_y/3 + d4_y/6
        z = z + d1_z/6 + d2_z/3 + d3_z/3 + d4_z/6

        print(t, y, z)

# euler(0, 0, 1, 0.25, func_y, func_z)
rk4(0, 0, 1, 0.25, func_y, func_z)

