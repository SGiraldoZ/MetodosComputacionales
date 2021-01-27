import numpy as np
import math

# ECUACION DIFERENCIAL SERÁ
#   Y' = funcion(x, y)

def funcion(x:float, y: float):
    # Escrbir en el return la función de la E.D

        return 0.026*(1-(y/12000))*y

def aproxEuler(h, xPrev, yPrev):
    f = funcion(xPrev, yPrev)
    print("f("+str(xPrev)+","+str(yPrev)+"): "+str(f))
    return yPrev + (h*f)

def euler(h, xInit, xFin, y0):
    r = [[],[]]
    r[0].append(xInit)
    r[1].append(y0)
    while(xInit <= xFin):
        xPrev = xInit
        yPrev = r[1][-1]
        xInit += h
        r[0].append(xInit)
        y = aproxEuler(h, xPrev, yPrev)
        r[1].append(y)

    return r

def eulerM(h, xInit, xFin, y0):
    r = [[],[]]
    r[0].append(xInit)
    r[1].append(y0)
    while(xInit <= xFin):
        xPrev = xInit
        yPrev = r[1][-1]
        xInit += h
        r[0].append(xInit)
        z = aproxEuler(h, xPrev, yPrev)
        y = yPrev + ((h/2)*(funcion(xPrev, yPrev)+funcion(r[0][-1], z)))
        r[1].append(y)

    return r

def RK4(h, xInit, xFin, y0):
    xs = [xInit]
    ys = [y0]
    while(xInit <= xFin):
        xPrev = xs[-1]
        yPrev = ys[-1]
        xInit += h
        xs.append(xInit)
        k1 = funcion(xPrev, yPrev)
        k2 = funcion(xPrev+(h/2), yPrev+(h*k1/2))
        k3 = funcion(xPrev+(h/2), yPrev+(h*k2/2))
        k4 = funcion(xPrev+h, yPrev+(h*k3))
        y  = yPrev + (h/6)*(k1+(2*k2)+(2*k3)+k4)
        ys.append(y)

    return [xs, ys]


def RK3(h, xInit, xFin, y0):
    xs = [xInit]
    ys = [y0]
    while(xInit <= xFin):
        xPrev = xs[-1]
        yPrev = ys[-1]
        xInit += h
        xs.append(xInit)
        k1 = h*funcion(xPrev, yPrev)
        k2 = h*funcion(xPrev+(h/2), yPrev+(k1/2))
        k3 = h*funcion(xPrev+(h), yPrev-k1+2*k2)

        y  = yPrev + (1/6)*(k1+(4*k2)+(k3))
        ys.append(y)

    return [xs, ys]




result = eulerM(5,0,120, 2555)
for n in range(len(result[0])):

    print(str(result[0][n])+"        "+str(result[1][n]))