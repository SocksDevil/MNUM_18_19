import math

def euler(t, y, h, func):
    for _ in range(0, 2):
        y = y + h * func(t, y)
        t += h
        print(t, y)



def rk4(t, y, h, func):
    for _ in range(0, 3):
        d1 = h * func(t, y)
        d2 = h * func(t + h/2, y + d1/2)
        d3 = h * func(t + h/2, y + d2/2)
        d4 = h * func(t + h, y + d3)
        print(t, y, d1, d2, d3, d4)
        y = y + 1/6*d1 + 1/3 * d2 + 1/3 * d3 + 1/6 * d4
        t += h

# euler(2, 2, 0.25, lambda t, y: y/(t - 1))
# rk4(2, 2, 0.25, lambda t, y: y/(t - 1))

# Uma forma de variar o lambda no metodo do gradiente seria avaliar a posiçao do novo ponto calculado antes de avançar.
# Comparando o valor deste, com o valor do ponto anteriormente calculado é possivel de saber se este se afastou ou se 
# aproximou do valor anteriormente calculado calculando o seu valor no ponto  e no ponto anterior. Caso o novo ponto seja
# maior, ou menor no caso de ser para o calculo do maximo e nao do minimo, esse passo não é tomado e o step é decrementado.
# Sempre que o passo é efetivamente tomado, o step é aumentado. Normalmente, este incremente e decremento é feito usando
# a multiplicação ou divisão por 2, respetivamente, uma vez que é uma operaçao que apenas implica um shift de bits
# para a esquerda ou direita, respetivamente.


def gradient(x, y, h, gradient, func):
    flag = False
    xn, yn = 0, 0
    while abs(xn - x) > 10**(-5) and abs(yn - y) > 10**(-5):
        if(flag):
            x, y = xn, yn
            break
        xn = x - h * gradient[0](x, y)
        yn = y - h * gradient[1](x, y)
        if(func(xn, yn) < func(x, y)):
            flag = True
            h*=2
        else:
            flag = False
            h/=2
    print(func(x, y))


# gradient(2.4, 4.3, 0.1, [lambda x, y: -1.7*y + 14 *x - 8, lambda x, y: -1.7 * x + 12], lambda x, y: -1.7*x*y + 12*y + 7*x*x - 8*x)

def exercise_5_1(x, y):
    return pow(x, 2) - y - 2

def exercise_5_1_dev_x(x, y):
    return 2 * x

def exercise_5_1_dev_y(x, y):
    return -1

def exercise_5_2(x, y):
    return -x + pow(y, 2) - 2

def exercise_5_2_dev_x(x, y):
    return -1

def exercise_5_2_dev_y(x, y):
    return 2 * y

def newton(x, y, f1, f1_x, f1_y, f2, f2_x, f2_y):
    for _ in range(0, 2):
        prev_x, prev_y = x, y
        x = prev_x - (f1(prev_x, prev_y) * f2_y(prev_x, prev_y) - f2(prev_x, prev_y) * f1_y(prev_x, prev_y))/(f1_x(prev_x, prev_y) * f2_y(prev_x, prev_y) - f2_x(prev_x, prev_y) * f1_y(prev_x, prev_y))
        y = prev_y - (f2(prev_x, prev_y) * f1_x(prev_x, prev_y) - f1(prev_x, prev_y) * f2_x(prev_x, prev_y))/(f1_x(prev_x, prev_y) * f2_y(prev_x, prev_y) - f2_x(prev_x, prev_y) * f1_y(prev_x, prev_y))
        print(x, y)

# newton(1.5, 0.8, exercise_5_1, exercise_5_1_dev_x, exercise_5_1_dev_y, exercise_5_2, exercise_5_2_dev_x, exercise_5_2_dev_y)

def simpson(a, b, h, func):
    n = int(abs(b - a)/h)
    integral = func(a) + func(b)
    values = []
    
    for i in range(1, n, 2):
        values.append(4 * func(a + i * h))
    
    for i in range(2, n, 2):
        values.append(2 * func(a + i * h))
    
    for i in values:
        integral+= i
    
    integral*=h/3

    return integral

print(simpson(2.5, 3, 0.125, lambda x: math.exp(1.5 * x)))
print(simpson(2.5, 3, 0.125/2, lambda x: math.exp(1.5 * x)))
print(simpson(2.5, 3, 0.125/4, lambda x: math.exp(1.5 * x)))