import math
def math_func(x):
    return (x - 2*math.log(x, math.exp(1))-5)

def math_func_dev(x):
    return (1- 2/x)

def math_g_func(x):
    return (2*math.log(x, math.exp(1))+5)

def math_g_sec_func(x):
    return math.exp((x-5)/2)

def math_g_sec_func_dev(x):
    return math.exp((x-5)/2)/2

def math_g_func_dev(x):
    return 2/x

#Using maxima it was determined the function had 2 zeros

# # 1st zero [0.01, 1]
# print(math_func(0.01))
# print(math_func(1))
#
# # 2st zero [9, 10]
# print(math_func(9))
# print(math_func(10))

def bissect(a, b, error, func):
    counter = 0
    while abs(a - b) > error:
        xn = (a+b)/2
        if(func(a)*func(xn) < 0):
            b = xn
        else:
            a = xn
        counter+=1
    print(counter)
    return (a+b)/2

def rope(a, b, error,func):
    counter = 0
    xn = 0
    while abs(xn-b) > error:
        xn = b
        b = ((a*func(b)-b*func(a))/(func(b)-func(a)))
        counter+=1
    print(counter)
    return b

# print(rope(0.01,1,10**(-5)))
# print(rope(9,10,10**(-5)))

#Testar diferentes critérios de paragem para ver se faz diferença

def newton(x,error, func):
    prev_x = 0;
    counter = 0;
    while abs(x-prev_x) > error:
        prev_x = x
        x = x - (func(x)/func(x))
        counter+=1
    print(counter)
    return x

# print(newton(3, 10**(-5)))

def picard_peano(x, error, func, func_dev):
    prev_x = 0
    counter = 0
    if(func_dev(x) >= 1):
        return "Impossible to solve with the method"
    while abs(x - prev_x) > error :
        prev_x = x
        x = func(x)
        counter+=1
    print(counter)
    return  x

print(picard_peano(0.01, 10**(-5), math_g_sec_func, math_g_sec_func_dev))