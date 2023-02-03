import random
import sys
import math
import random
import numpy
import csv as c
import time

#Require: Un valor primo p, un generador αlpha de Z
#Require: Un valor β de Z

def baby(p,alpha,beta):
    n= math.ceil(math.sqrt(p))

    T = []
    for r in range (1,n):
        expo = pow(alpha,r,p)
        t = [expo,r]
        T.append(t)
    negexp = pow(alpha, n*(p-2), p) ## Equivalente a alpha^-n mod p
    gamma = beta

    d = dict(T)


    for q in range(0,n-1):

        if gamma in d:
            return (q*n + d[gamma]) #retornamos k
        gamma = (gamma * negexp)%p

    return False #No ha encontrado la solucion








def cargarDatos():
    file_name = "input.csv"
    with open(file_name, encoding="UTF8") as csv_file:
        csv_reader = c.reader(csv_file)
        data = list(csv_reader)
    return data


m = cargarDatos()

tiempo = 0
print("Nºbits,p,k,tiempo")
M = []

def crearDatos():
    for i in m:
        nbits = int(i[0])
        numero = int(i[1])
        alpha = int(i[2])
        beta = int(i[3])
        start = time.time()
        k = baby(numero,alpha,beta)
        end = time.time()
        tiempo = end - start
        v = [nbits, numero, k, tiempo]
        print(v)
        M.append(v)

crearDatos()
cabecera = ["Nºbits","p","k","tiempo"]
def crearCSV():
    myfile = open("output.csv","w",  newline='')
    with myfile:
        writer = c.writer(myfile)
        writer.writerow(cabecera)
        writer.writerows(M)

crearCSV()

"""
32, 2703258601, 87, 1218285964, 1351629300
36, 66993967457, 100, 30349383276, 33496983728
40, 927498176207, 100, 28012336526, 463749088103
44, 10876265372701, 91, 2344566393258, 5438132686350
48, 149883250766927, 100, 59398595592256, 74941625383463
"""
