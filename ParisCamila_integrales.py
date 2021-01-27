import numpy as np
import matplotlib.pyplot as plt
#limites de integracion
ini=-np.pi/2
end=np.pi
#numero de puntos, defino h y x para la funcion
pts=10001
h1=(end-ini)/(pts-1)
x1 = np.linspace(ini,end,pts)
#funcion de cos(x)
def fun(x):
    return np.cos(x)
#integral analitica de cos(x)
def IntAnalitica(min, max):
    return np.sin(max)-np.sin(min)
#metodo para integral con el metodo del trapezoide
def IntTrapezoide(funcion,h,x):
    y=funcion(x)
    integral=(y.sum()-y[0]-y[-1])*h + (y[0]+y[-1])*h/2
    return integral
#metodo para integral con el metodo de simpson
def IntSimpson(funcion,h,x):
    y = funcion(x)
    integral=((y[0]+y[-1])*h/3.0+sum(y[1:-1:2]*4*h/3.0)+sum(y[2:-2:2]*2*h/3.0))
    return integral
#metodo para integral con el metodo de Monte Carlo
def IntMonteCarlo(funcion,numpts,mn,mx):
    xm = np.linspace(mn,mx,numpts)
    y = funcion(xm)
    min_y = 0.0
    max_y = np.amax(y)
    n_random = numpts
    random_x1 = np.random.rand(int(n_random)) * (mx - mn) + mn
    random_y1 = np.random.rand(int(n_random)) * (max_y - min_y) + min_y
    delta = fun(random_x1) - random_y1
    below  = np.where(delta>0.0)
    interval_integral = (max_y-min_y) * (mx - mn)
    integral1  = interval_integral * (np.size(below)/(1.0*np.size(random_y1)))
    max_y2 = 0.0
    min_y2 = -np.amax(y)
    random_x2 = np.random.rand(int(n_random)) * (mx - mn) + mn
    random_y2 = np.random.rand(int(n_random)) * (max_y2 - min_y2) + min_y2
    delta = fun(random_x2) - random_y2
    below  = np.where(delta<0.0)
    interval_integral = (max_y-min_y) * (mx - mn)
    integral2  = interval_integral * (np.size(below)/(1.0*np.size(random_y2)))
    return (integral1-integral2)
#metodo para integral con el metodo de valores medios
def IntValoresM(funcion, max, min, Pts):
    x2 = np.random.random(int(Pts)) * (max - min) + (min)
    y = funcion(x2)
    integral = np.average(y) * (max-min)
    return integral
#imprimo el metodo de integracion, el resultado y el error respecto a la analitica
print("metodo: Trapezoide,", IntTrapezoide(fun,h1,x1),",", abs(IntTrapezoide(fun,h1,x1)-IntAnalitica(ini,end))/IntAnalitica(ini, end))
print("metodo: Simpson,", IntSimpson(fun,h1,x1),",", abs(IntSimpson(fun,h1,x1)-IntAnalitica(ini,end))/IntAnalitica(ini, end))
print("metodo: Monte Carlo,", IntMonteCarlo(fun,pts,ini,end),",", abs(IntMonteCarlo(fun,pts,ini,end)-IntAnalitica(ini,end))/IntAnalitica(ini, end))
print("metodo: Valores Medios,", IntValoresM(fun,end,ini,pts),",", abs(IntValoresM(fun,end,ini,pts)-IntAnalitica(ini,end))/IntAnalitica(ini, end))
#numero de puntos de 101 a 1+10**7
NPts=np.logspace(2.0, 7.0, num = 6, base=10.0)+1
#retorna el error con el metodo del trapezoide para los numeros de puntos anteriores 
def listaErrorT(func, min, max):
    listaErrorT=[]
    for i in range(6):
        H=(max-min)/(NPts[i]-1)
        xe = np.linspace(min,max,NPts[i])
        errort = abs(IntTrapezoide(func,H,xe)-IntAnalitica(min,max))/IntAnalitica(min, max)
        listaErrorT.append(errort)
    return listaErrorT
#grafica el error en funcion del numero de puntos
plt.figure()
a=listaErrorT(fun,ini,end )
plt.loglog(NPts,a,c="r")
#retorna el error con el metodo del simpson para los numeros de puntos anteriores 
def listaErrorS(min,max,func):
    listaErrorS=[]
    for i in range(6):
        H=(max-min)/(NPts[i]-1)
        xe = np.linspace(min,max,NPts[i])
        errors = abs(IntSimpson(func,H,xe)-IntAnalitica(min,max))/IntAnalitica(min, max)
        listaErrorS.append(errors)
    return listaErrorS
#grafica el error en funcion del numero de puntos
b=listaErrorS(ini,end,fun)
plt.loglog(NPts,b, c="g")
#retorna el error con el metodo de Monte Carlo para los numeros de puntos anteriores 
def listaErrorM(min,max,func):
    listaErrorM=[]
    for i in range(6):
        puntos=NPts[i]
        xe = np.linspace(min,max,NPts[i])
        errors = abs(IntMonteCarlo(func,puntos,min,max)-IntAnalitica(min,max))/IntAnalitica(min, max)
        listaErrorM.append(errors)
    return listaErrorM
#grafica el error en funcion del numero de puntos
d=listaErrorM(ini,end,fun)
plt.loglog(NPts,d, c="black")
#retorna el error con el metodo de valores medios para los numeros de puntos anteriores 
def listaErrorV(min,max,func):
    listaErrorV=[]
    for i in range(6):
        puntos=NPts[i]
        H=(max-min)/(puntos-1)
        xe = np.linspace(ini,end,puntos)
        error = abs(IntValoresM(func,end,ini,puntos)-IntAnalitica(min,max))/IntAnalitica(min, max)
        listaErrorV.append(error)
    return listaErrorV
#grafica el error en funcion del numero de puntos
c=listaErrorV(ini,end,fun)
plt.loglog(NPts,c,c="blue")
plt.grid()
plt.savefig("ParisCamila_int_error.pdf")
#funcion 1/raiz de sin(x)
def funcionSqrtSin(x):
    return (1/(np.sqrt(np.sin(x))))
#limites de integracion, numero de puntos, x, h 
lim_inf=0.0
lim_sup=1.0
pts3=10000000
x3=np.linspace(lim_inf,lim_sup,pts3)
h3=(lim_sup-lim_inf)/(pts3-1)
lim_infsmall=10**(-6)
#cambiando inf por 10**6
def IntSimpsonValorGrande(funcion,h,x):
    y = funcion(x)
    y[0]=10**6
    integral=(((y[0]+y[-1])*h/3.0)+sum(y[1:-1:2]*4*h/3.0)+sum(y[2:-2:2]*(2*h)/3.0))
    return integral
print(lim_sup-lim_inf)
print("El nuevo valor de la integral usando el metodo de Simpson cambiando infinito por", 10**6, "el valor de la integral es",IntSimpsonValorGrande(funcionSqrtSin,h3,x3))
#x y h para cambio de 0 a 10**(-6)
xp4=np.linspace(lim_infsmall,lim_sup,pts)
h4=(lim_sup-lim_infsmall)/(pts-1)
print("El nuevo valor de la integral usando el metodo de Simpson evaluando la funcion en", 10**(-6), "y no en cero el valor de la integral es", IntSimpson(funcionSqrtSin,h4,xp4))
#funcion de la aproximacion de valores pequenos de x
def funAproxSin(x):
    return((1/(np.sqrt(np.sin(x))))-1/np.sqrt(x))
integralSqrtXParte2=2.0

#Utilice x y h con el limite inferior 10**(-6) porque intente calcularla de cero a uno y las singularidades no se cancelaban. Aqui muestro la suma del valor analitico de la segunda parte con el numerico de la primera.
print("Restando la singularidad el resultado es", IntSimpson(funAproxSin,h4,xp4)+integralSqrtXParte2)
print("El metodo que mas se acerca a 2.03480532 fue el ultimo, en el de la aproximacion de valores pequenos")
#Aqui hago el punto 3c-1(Probar los metodos con la integral dada pero saca error por la division por cero). Solo el de valores medios saca el valor.
#print(IntTrapezoide(funcionSqrtSin,h3,x3),IntSimpson(funcionSqrtSin,h3,x3),IntMonteCarlo(funcionSqrtSin,pts,lim_inf,lim_sup),IntValoresM(funcionSqrtSin, lim_sup, lim_inf, pts))




