import numpy as np
import copy

# DESPUES DE LOS METODOS Y LA CLASE ESTA EL SCRIPT QUE SE EJECUTA


#   CODIGO PARA LA SOLUCION DE SISTEMAS:
class ENotReady(Exception):

    def __init__(self):
        super().__init__("Porfa escoges un metodo para crear T y C todo bien ;)")

class Sistema:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.inicializar()
        self.readyToSolve = False
        return

    def inicializar(self):
        self.u = -np.triu(self.a, k=1)
        self.l = -np.tril(self.a, k=-1)
        self.d = np.diagflat(np.diag(self.a))
        return

    def initSOR(self, w=1):
        invDwL = np.linalg.inv(np.subtract(self.d, (w*self.l)))
        self.t = np.matmul(invDwL, ((1-w)*self.d+w*self.u))
        self.c = w*np.matmul(invDwL, self.b)
        self.readyToSolve = True
        return

    def initGaussSeidel(self):
        self.initSOR()
        return

    def initJacobi(self):
        self.t = np.matmul(np.linalg.inv(self.d),np.add(self.l,self.u))
        self.c = np.matmul(np.linalg.inv(self.d),self.b)
        self.readyToSolve = True
        return

    def solve(self, xPrev,iAct, iterations=500, delta=0.00001, tolerancia=0.00001):
        # print(xPrev)
        # print(iAct)
        if(not self.readyToSolve):
            raise ENotReady
        if(iAct == iterations):
            print("Limite de iteraciones alcanzado")
            return None
#         NO SE HA ALCANZADO EL LIMITE DE ITERACIONS Y EL SISTEMA TIENE TODO LO QUE SE NECESITA PARA RESOLVER
        x = np.add(np.matmul(self.t, xPrev), self.c)
        error = np.linalg.norm(np.subtract(x, xPrev))
        AxMinB = np.subtract(np.matmul(self.a, x), self.b)
        fx = np.linalg.norm(AxMinB)
        print("iteracion "+str(iAct)+": " +str(x))
        if(fx <= delta or error <= tolerancia):
            print("Iteraciones: "+str(iAct))
            print("Error: " + str(error))
            print("|AX-b|: "+str(fx))
            return x

        return self.solve(x, iAct+1,iterations=iterations, delta=delta, tolerancia=tolerancia)

    def Jacobi(self, xInit=None, iterations=500, delta=0.00001, tolerancia=0.00001):
        self.initJacobi()
        if(xInit == None):
            xInit = np.zeros(len(self.b))
        return self.solve(xInit,0,iterations=iterations, delta=delta, tolerancia=tolerancia)

    def Gauss_Seidel(self, xInit=None, iterations=500, delta=0.00001, tolerancia=0.00001):
        self.initGaussSeidel()
        if(xInit == None):
            xInit = np.zeros(len(self.b))
        return self.solve(xInit,0,iterations=iterations, delta=delta, tolerancia=tolerancia)

    def SOR(self,w, xInit=None, iterations=500, delta=0.00001, tolerancia=0.00001):
        self.initSOR(w=w)
        if(xInit == None):
            xInit = np.zeros(len(self.b))
        return self.solve(xInit,0,iterations=iterations, delta=delta, tolerancia=tolerancia)



def permutaciones(n: []):
    if(len(n)>2):
        r = []
        for e in range(len(n)):
            rPrev = permutaciones(n[0:e]+n[e+1:])
            for array in rPrev:
                r.append([n[e]]+array)
        return r
    else:
        return [n, n[::-1]]

def listaInds(n):
    l = []
    for i in range(n):
        l += [i]
    return l

def fullSolve(a, b,xInit=None, iterations=500, delta=0.00001, tolerancia=0.00001):
    permInds = permutaciones(listaInds(len(a)))
    sln = None
    a0 = copy.deepcopy(a)
    b0 = copy.deepcopy(b)
    permAct = 0
    while(sln is None and permAct < len(permInds)):
        w = 0.01
        for n in range(len(a)):
            a[n] = a0[permInds[permAct][n]]
            b[n] = b0[permInds[permAct][n]]
        print("Sistema: "+str(a)+"; b: "+str(b))
        s = Sistema(a,b)
        while(sln is None and w < 2):
            print("w: "+str(w))
            sln = s.SOR(w, xInit=xInit, iterations=iterations, delta=delta, tolerancia=tolerancia)
            # print(sln)
            w = round(w+0.01,3)
        permAct += 1

    if (sln is not None):
        print("Se resolvio el sistema: "+str(a)+"; b: "+str(b))
        print("\nY w: "+str(w))
    return sln



# SCRIPT QUE SE EJECUTA:

a = [[-4,1,1,0],[1,-4,0,1],[1,0,-4,1],[0,1,1,-4]]


b = [0,-50,-150,-200]

s = Sistema(a,b)
print(s.Jacobi())

# FIN DEL CODIGO QUE SE EJECUTA
