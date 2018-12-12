import math

def math_ex_1(x):
    return pow(pow(x,3) * 4 - x + 1 , 0.25)

def picard_peano(x, func, error):
    prev_x = 0
    while abs(x - prev_x) > error:
        prev_x = x
        print(x)
        x = func(x)
    return x

# picard_peano(4, math_ex_1, 10**(-5))


######## Pergunta 4 ##############
# A utilização da equação a traz uma série de vantagens relativamente ao uso da equação b, uma vez que a 
# equação b apresenta uma função discontínua, que apresenta um declive muito elevado. Na aplicação do método de
# Newton, ao traçar uma tangente, esta irá ter dificuldades em aproximar-se do valor desejado, podendo até mesmo
# não conseguir alcançar após várias iterações.
# A equação a é muito mais estável nesse sentido, pelo o que o método de newton conseguirá aproximar-se do valor
# desejado em menos iterações
# 
def math_ex_7(x):
    return -x + 60 *  math.cos(math.sqrt(x)) + 2
def math_ex_dev_7(x):
    return (- 30 * math.sin(math.sqrt(x)))/(math.sqrt(x)) - 1

def newton(x, func, func_dev, error):
    prev_x = 0
    while abs(x - prev_x) > error:
        prev_x = x
        print(x, func(x))
        x = prev_x - func(prev_x)/func_dev(prev_x)
    return x
# newton(1.8, math_ex_7, math_ex_dev_7, 10**(-5))

def exercise_6(x):
    return x + pow(x-2, 2)/(math.sin(x) + 4)

def aurea(x1, x2, func, error):
    B = (math.sqrt(5) - 1)/2
    A = B * B
    counter = 0
    while abs(x1 - x2) > error and counter < 3:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        counter+=1
        print(x1, x2, x3, x4, func(x1), func(x2), func(x3), func(x4))
        if(func(x3) < func(x4)):
            x2 = x4
        else:
            x1 = x3
    
# aurea(-1, 1.5, exercise_6, 10**(-3))