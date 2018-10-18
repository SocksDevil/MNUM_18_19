import math

def g1_func_x(x,y):
    return y/2 - 1/ (2*x) + 5/2

def func_dev_g1_x(x,y):
    return 1/2

def func_dev_g1_y(x,y):
    return 1/ (2*pow(x,2))

def func_dev_g2_x(x,y):
    return (3/x+1)/(2 * math.sqrt(3*math.log(x)+x))

def func_dev_g2_y(x,y):
    return 0

def g2_func_y(x,y):
    return math.sqrt(x + 3*math.log(x))





def picard_peano(x, y, func_g1_x, func_g2_y, func_dev_g1_x, func_dev_g1_y, func_dev_g2_x, func_dev_g2_y, error):
    if(func_dev_g1_x(x,y) >= 1 or func_dev_g1_y(x,y) >= 1 or func_dev_g2_x(x,y) >=1 or func_dev_g2_y(x,y) >=1):
        return "Impossible to solve"
    prev_x = 0
    prev_y = 0
    while (abs(x-prev_x) > error) and (abs(y-prev_y)) > error:
        prev_x = x
        prev_y = y
        x = func_g1_x(x,y)
        y = func_g2_y(x,y)
    return x,y


print(picard_peano(4,4,g1_func_x, g2_func_y, func_dev_g1_x, func_dev_g1_y, func_dev_g2_x, func_dev_g2_y, 10**(-5)))