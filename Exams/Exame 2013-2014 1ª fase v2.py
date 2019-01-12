import math

def exercise_1_g(x):
    return pow(4*pow(x,3) - x + 1, 1/4)

def picard_peano(x, func):
    for _ in range(0, 2):
        print(x)
        x = func(x)
    print(x)

# picard_peano(4, exercise_1_g)

# Exercicio 4
# Após a analise do grafico da função a) é possivel observar que ela possui um declive significativamente vertical o 
# que cria a necessidade de escolher um guess inicial adequado a que este declive nao possua uma grande influencia.
# A analise do grafico b) possui um ponto de descontinuidade que não será um problema para o método em questão.
# No entanto, o mesmo problema relacionado com o declive apresenta-se, desta vez sobre a forma horizontal, o que
# se prova mais uma vez um desafio para um metodo de newton, cujo grande objetivo será calcular tangentes consecutivas
# numa tentativa de aproximação do valor da raiz.


# Exercicio 5
# Para o cálculo de integrais são conhecidos dois métodos: método dos trapezios e o metodo de simspon. Sobre
# estes é também conhecido o seu valor de ordem, respetivamente 2 e 4. Deste modo, é sabido que o calculo
# do quociente de convergencia de um algoritmo de ordem n é: QC: (s' - s)/(s" - s'). Sabendo que QC tem de ser
# aproximadamente igual a 2 ^ n
# Deste modo, era possível escolher um destes métodos e calcular o valor do integral para h, para 
# h/2 e h/4, sendo cada um destes s, s' e s" respetivamente. Assim, seria possivelmente calcular o 
# quociente de convergencia do mesmo e deste determinar a qualidade da informação do integral.
# Do mesmo modo seria possivel calcular o erro com E: (s" - s')/(2^n-1). Deste modo, podia parar quando o erro fosse 
# suficientemente baixo para o critério definido e a precisão necessária.


def exercise_6(x):
    return x + pow(x-2, 2)/(math.sin(x) + 4)

def aurea(x1, x2, func, error):
    B = (math.sqrt(5) - 1)/2
    A = B * B
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        print(x1, x2, x3, x4, func(x1), func(x2), func(x3), func(x4))
        if(func(x3) < func(x4)):
            x2 = x4
        else:
            x1 = x3
        

# aurea(-1, 1.5, exercise_6, 10**(-5))

def exercise_7(x):
    return -x + 60 * math.cos(math.sqrt(x)) + 2

def exercise_7_dev(x):
    return - (30 * math.sin(math.sqrt(x))/math.sqrt(x)) - 1

def newton(x, func, func_dev):
    for _ in range(0, 3):
        print(x, func(x))
        x = x - func(x)/func_dev(x)

newton(1.8, exercise_7, exercise_7_dev)
