import math

def func_dev_x(x , y, t):
    return x

def func_dev_y(x , y, t):
    return 0.5 + pow(t, 2) + t * x

def euler(x, y, t, h, func_dev_x, func_dev_y):
    for _ in range(0, 2):
        print(t, x, y)
        prev_x, prev_y = x, y
        x = x + h * func_dev_x(prev_x, prev_y, t)
        y = y + h * func_dev_y(prev_x, prev_y, t)
        t+= h
    print(t, x, y)

# euler(1, 0, 1, 0.25, func_dev_x, func_dev_y)

def rk4(x, y, t, h, func_dev_x, func_dev_y):
    for _ in range(0, 2):
        print(t, x, y)
        d1_x = h * func_dev_x(x, y, t)
        d1_y = h * func_dev_y(x, y, t)

        d2_x = h * func_dev_x(x + d1_x/2, y + d1_y/2, t + h/2)
        d2_y = h * func_dev_y(x + d1_x/2, y + d1_y/2, t + h/2)

        d3_x = h * func_dev_x(x + d2_x/2, y + d2_y/2, t + h/2)
        d3_y = h * func_dev_y(x + d2_x/2, y + d2_y/2, t + h/2)

        d4_x = h * func_dev_x(x + d3_x, y + d3_y, t + h)
        d4_y = h * func_dev_y(x + d3_x, y + d3_y, t + h)

        x = x + 1/6 * d1_x + 1/3 * d2_x + 1/3 * d3_x + 1/6 * d4_x
        y = y + 1/6 * d1_y + 1/3 * d2_y + 1/3 * d3_y + 1/6 * d4_y
        t+=h
    print(t, x, y)

# rk4(1, 0, 1, 0.25, func_dev_x, func_dev_y)
    



# Exercicio 2 
# Uma vez que pivotagem parcial é metodo em que se escolhe não o primeiro coeficiente não nulo
# mas sim o que tenha o maior valor absoluto. Deste modo, são reduzidos várias erros devido à 
# precisão da máquina. Uma vez que a primeira equação apresenta um valor do 1º coeficiente extremamente
# baixo, esta, numa abordagem sem pivotagem, iria certamente trazer erros associados à maquina que fariam
# com que o resultado se afastasse do valor real.
# Assim, é possivel concluir que o resultado com pivotagem será a solução mais correta.


def func_3_dev_x(x, y):
    return 6 * x - y - 8

def func_3_dev_y(x, y):
    return -x + 11 + 2*y

def exercise_3(x, y):
    return 3 * pow(x, 2) - x * y + 11 * y + pow(y,2) - 8 * x

def gradient(x, y, h, gradient,func, error):
    xn, yn = 0,0 
    counter = 0
    flag = False
    while abs(xn - x) > error or (abs(yn - y) > error):
        counter+=1
        if(flag):
            x, y = xn, yn
        xn = x - h * gradient[0](x, y)
        yn = y - h * gradient[1](x, y)
        if(func(xn, yn) < func(x, y)):
            flag = True
            h*=2
        else:
            flag = False
            h/=2
        print(x, y)
    print(x, y, counter)

# gradient(2, 2, 0.5, [func_3_dev_x, func_3_dev_y], exercise_3, 10**(-5))

def exercise_4(x):
    return math.exp(1.5*x)

def simpson(a, b, h, func):
    n = int(abs(a - b)/h)
    area = 0
    values = []
    for i in range(1, n, 2):
        values.append(func(a + i * h) * 4)

    for i in range(2, n, 2):
        values.append(func(a + i * h) * 2)

    area+= func(a) + func(b)
    
    for i in values:
        area+=i
    area*=h/3
    return area

# print(simpson(1, 1.5, 0.125, exercise_4))
# print(simpson(1, 1.5, 0.125/2, exercise_4))
# print(simpson(1, 1.5, 0.125/4, exercise_4))
def exercise_5(x):
    return (x - 3.7) + pow(math.cos(x + 1.2), 3)

def exercise_5_dev(x):
    return 1 - 3 * pow(math.cos(x + 1.2), 2) * math.sin(x + 1.2)

def newton_first_iter(x, func, func_dev):
    return (x - (func(x)/func_dev(x)))

# print(newton_first_iter(3.8, exercise_5, exercise_5_dev))
