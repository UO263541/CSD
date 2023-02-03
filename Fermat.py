import sys
import math
import numpy
import time
import csv as c
#Require: Un número entero positivo compuesto n
#Ensure factores a y b de n


def raizSuperior(n):
    radical = math.sqrt(n)
    entero = int(radical)
    resto = radical%entero
    if (resto==0):
        return entero
    else:
        return entero+1

def esCuadradoPerfecto(n):
    radical = math.sqrt(n)
    entero = int(radical)
    resto = radical % entero
    if (resto==0):
        return True
    else:
        return False



def Fermat(n):
    #Primo n
    A = raizSuperior(n)
    B = (A * A) - n


    while (not(esCuadradoPerfecto(B)) ):
        A+=1
        B = (A * A) - n

    radical = math.sqrt(B)
    radical = int(radical)
    v=[A-radical,A+radical]
    return v

print(Fermat(44461))
print(Fermat(2534389177))

start = time.time()

end = time.process_time()

print("Tiempo: ",end-start)


def cargarDatos():
    file_name = "input.csv"
    with open(file_name, encoding="UTF8") as csv_file:
        csv_reader = c.reader(csv_file)
        data = list(csv_reader)
    return data


m = cargarDatos()
tiempo = 0
print("Nºbits,n,factor1,factor2,tiempo")
M = []
def crearDatos():
    for i in m:
        nbits = int(i[0])
        numero = int(i[1])
        start = time.time()
        factores = Fermat(numero) #cambiar los factores para que no sea un vector, para el csv
        end = time.time()
        tiempo = end-start
        v = [nbits,numero,factores[0],factores[1],tiempo]
        print(v)
        M.append(v)


crearDatos()
print(M)
def crearCSV():
    myfile = open("output.csv","w",  newline='')
    with myfile:
        writer = c.writer(myfile)
        writer.writerows(M)


crearCSV()

