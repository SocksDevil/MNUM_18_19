import math

def g1_original(x,y):
    return pow(x,2)*2 - x * y - 5*x + 1
def g1_original_dev_x(x,y):
    return 4*x - y - 5

def g2_original(x,y):
    return x + 3 * math.log(x) - pow(y,2)

def g2_original_dev_y(x,y):
    return -2*y

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

def g3_func_y(x,y):
    return (x+3*math.log(x))/y

def func_dev_g3_x(x,y):
    return (3/x + 1)/y

def func_dev_g3_y(x, y):
    return -(3*math.log(x) + x)/(y**2)




def picard_peano(x, y, func_g1_x, func_g2_y, func_dev_g1_x, func_dev_g1_y, func_dev_g2_x, func_dev_g2_y, error):
    if(func_dev_g1_x(x,y) >= 1 or func_dev_g1_y(x,y) >= 1 or func_dev_g2_x(x,y) >=1 or func_dev_g2_y(x,y) >=1):
        return "Impossible to solve"
    prev_x = 0
    prev_y = 0
    counter = 0
    while (abs(x-prev_x) > error) or (abs(y-prev_y)) > error:
        prev_x = x
        prev_y = y
        x = func_g1_x(prev_x,prev_y)
        y = func_g2_y(prev_x, prev_y)
        counter+=1
    return x,y,counter


print(picard_peano(4,4,g1_func_x, g2_func_y, func_dev_g1_x, func_dev_g1_y, func_dev_g2_x, func_dev_g2_y, 10**(-5)))


def newton(x, y, func_g1_x, func_g2_y, func_dev_g1_x, func_dev_g2_y, error):
    prev_x = 0
    prev_y = 0
    counter = 0
    while (abs(x-prev_x) > error) or (abs(y-prev_y)) > error:
        prev_x = x
        prev_y = y
        counter+=1
        x = prev_x -  (func_g1_x(x,y)/func_dev_g1_x(prev_x,prev_y))
        y = prev_y -  (func_g2_y(x,y)/func_dev_g2_y(prev_x, prev_y))
    return x, y, counter

print(newton(4, 4, g1_original, g2_original, g1_original_dev_x, g2_original_dev_y, 10**(-5)))