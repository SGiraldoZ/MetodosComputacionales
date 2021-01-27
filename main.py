from SistemasEcuaciones import Sistema
import numpy as np
# Press the green button in the gutter to run the scr.
if __name__ == '__main__':
    print("Ingrese la matriz de coeficientes como un arreglo de filas, asi: 1,2,3;4,5,6;7,8,9")
    print("Que es:   1  2  3")
    print("          4  5  6")
    print("          7  8  9")

    strA = input("Matriz: ")
    a = []
    for line in strA.split(";"):
        matLine = line.split(",")
        l = []
        for n in matLine:
            l.append(float(n))
        a.append(l)
    a = np.array(a)

    b = []

    strB = input("Ingrese el vector de términos independientes, con los elementos separados por comas: ")

    for e in strB.split(","):
        b.append(float(e))
    b=np.array(b)

    w = float(input("W para S.O.R: "))


    s = Sistema(a,b)

    sln = s.SOR(w)

    print(sln)

