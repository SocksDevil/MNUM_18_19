import math

def euler(fy, fz, xn, xf, yn, zn, h):
    n = (xf-xn)/h
    if (1.0 - abs(float(int(n)) - n)) <= 10**(-2):
        n = 1 + int(n)
    else:
        n = int(n)

    for i in range(n):
        oxn, oyn, ozn = xn, yn, zn

        zn = ozn + h*fz(oxn, oyn, ozn)
        yn = oyn +h*fy(oxn,oyn, ozn)
        xn = oxn + h

    return xn,yn,zn

def rk2(fy, fz, xn, xf, yn, zn, h):
    n = (xf-xn)/h
    if (1.0 - abs(float(int(n)) - n)) <= 10**(-2):
        n = 1 + int(n)
    else:
        n = int(n)

    print(n)
    for i in range(n):
        oxn, oyn, ozn = xn, yn, zn

        ay = oyn+h/2*fy(oxn, oyn, ozn)
        az = ozn+h/2*fz(oxn, oyn, ozn)

        zn = ozn + h*fz(oxn+h/2, ay, az)
        yn = oyn + h*fy(oxn+h/2, ay, az)
        
        xn = xn + h
    return xn, yn, zn

def rk4(fy, fz, xn, xf, yn, zn, h):
    n = int((xf-xn)/h)
    # if (1.0 - abs(float(int(n)) - n)) <= 10**(-5):
    #     n = 1 + int(n)
    # else:
    #     n = int(n)

    for i in range(n):
        dy1 = h*fy(xn, yn, zn)
        dz1 = h*fz(xn, yn, zn)

        dy2 = h*fy(xn + h/2, yn+dy1/2, zn+dz1/2)
        dz2 = h*fz(xn + h/2, yn+dy1/2, zn+dz1/2)

        dy3 = h*fy(xn + h/2, yn+dy2/2, zn+dz2/2)
        dz3 = h*fz(xn + h/2, yn+dy2/2, zn+dz2/2)

        dy4 = h*fy(xn + h, yn+dy3, zn+dz3)
        dz4 = h*fz(xn + h, yn+dy3, zn+dz3)

        xn = xn + h
        yn = yn + 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        zn = zn + 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
    return xn, yn, zn

def func_z(x,y,z):
    return x+y+z

def func_y(x,y,z):
    return x*y-z

def func_y_x(x,y,z):
    return z

def func_z_x(x,y,z):
    return x - 3 * z - 2 * y

# print(rk4(func_y_x, func_z_x, 0, 0.5, 0, 0, 0.05))

def calculate_qc_and_error(func_y_x, func_z_x, xn, xf, yn, zn, h, denom, method):
    _,s_y, s_z = method(func_y_x, func_z_x, xn, xf, yn, zn, h)
    _,s_line_y, s_line_z = method(func_y_x, func_z_x, xn, xf, yn, zn, h/2)
    _,s_double_line_y, s_double_line_z =method(func_y_x, func_z_x, xn, xf, yn, zn, h/4)
    qc_y = (s_line_y - s_y)/(s_double_line_y - s_line_y)
    qc_z = (s_line_z - s_z)/(s_double_line_z - s_line_z)
    error_y = (s_double_line_y - s_line_y)/denom
    error_z = (s_double_line_z - s_line_z)/denom
    return qc_y, qc_z, error_y, error_z

print(calculate_qc_and_error(func_y_x, func_z_x, 0, 0.5, 0, 0, 0.05, 15, rk4))