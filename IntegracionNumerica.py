import numpy as np

# IMPORTANTISIMO CAMBIAR EL METODO FUNCION

# TODOS LOS METODOS RESUELVEN LA INTEGRAL DE ESA FUNCION


def funcion(x):
    return (np.sqrt(np.exp(x-3)+(x**2)-1))

def trapecio(xInit, xFin):
    return (xFin-xInit)*(funcion(xInit)+funcion(xFin))/2

def formTrapecioCompuesto(puntos):
    r = 0
    for i in (range(0,len(puntos)-1)):
        r+= trapecio(puntos[i], puntos[i+1])


    return r

def trapecioCompuestoR(aproxPrev, puntos, iAct, iteraciones=100000, tolerancia = 1e-6):
    aprox = formTrapecioCompuesto(puntos)
    error = abs(aprox-aproxPrev)
    if(iAct < iteraciones and error > tolerancia):
        nuevosPuntos = partirPuntos(puntos)
        return trapecioCompuestoR(aprox, nuevosPuntos, iAct+1, iteraciones=iteraciones, tolerancia=tolerancia)
    else:
        return aprox
    # else:
    #     return None


def trapecioCompuesto(xInicio, xFin, iteraciones = 100000, tolerancia = 1e-6):
    aprox0 = trapecio(xInicio, xFin)
    return trapecioCompuestoR(aprox0, partirPuntos([xInicio,xFin]), 0, iteraciones=iteraciones, tolerancia=tolerancia)

def partirPuntos(puntos0):
    puntos = [puntos0[0]]
    for i in range(0, (len(puntos0)-1)):
        xMed = (puntos0[i]+puntos0[i+1])/2
        puntos.append(xMed)
    puntos.append(puntos0[-1])
    return puntos

def areaBajoParabola(x1, x2, x3):
    h = x2 - x1
    y1 = funcion(x1)
    y2 = funcion(x2)
    y3 = funcion(x3)
    return (h/3)*(y1+4*y2+y3)

def iterSimpson(puntos):
    puntosMedios = np.array(range(len(puntos)))[1:-1:2]# operacion con listas para conseguir los puntos medios de las parabolas
    aprox = 0
    for i in puntosMedios:
        aprox += areaBajoParabola(puntos[i-1], puntos[i], puntos[i+1])

    return aprox


def simpson(puntos, iteraciones = 1000, tolerancia = 1e-6):
    aprox0 = iterSimpson(puntos)
    nuevosPuntos = partirPuntos(puntos)
    return simpsonR(aprox0,nuevosPuntos, 0, iteraciones=iteraciones, tolerancia=tolerancia)


def simpsonR(aproxPrev, puntos, iAct, iteraciones=10000, tolerancia=1e-6):
    aprox = iterSimpson(puntos)
    error = np.abs(aprox-aproxPrev)
    if (iAct < iteraciones and error > tolerancia):
        nuevosPuntos = partirPuntos(puntos)
        return simpsonR(aprox, nuevosPuntos, iAct+1, iteraciones=iteraciones, tolerancia=tolerancia)
    else:
        return aprox

# print(trapecioCompuesto(3.1,4.9, tolerancia=1e-6))

print(iterSimpson([0.97,2.265,2.45]))
