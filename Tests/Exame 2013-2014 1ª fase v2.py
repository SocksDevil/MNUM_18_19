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
newton(1.8, math_ex_7, math_ex_dev_7, 10**(-5))