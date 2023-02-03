import random
import sys
import math
import random
import numpy

#Require: Un valor primo p, un generador α de Z
#Require: Un valor β de alpha generador
# Se supone conocido el orden de alpha
#Obtiene k que cumple el LD
def Pollard(p,alpha,beta,o):
    print("Primo p:",p)
    print("alpha:",alpha)
    print("beta:",beta)
    print("orden o:",o )

    a=b=aa=bb=0
    i=x=xx=1

    while(i<p):
        x,a,b = f(x,a,b,p,o,alpha,beta)
        xx,aa,bb = f(xx,aa,bb,p,o,alpha,beta)
        xx,aa,bb = f(xx, aa, bb, p, o, alpha, beta)


        if x == xx:
            if (math.gcd(b-bb,o)!=1):
                return False
            first=aa-a
            seg=b-bb
            FLT = pow(o+seg,1 * (o-2), o)
            t = (first * FLT) % o
            return t



    return False




def f(x,a,b,p,o,alpha,beta):
    #Clasificación de los valores en los 3 bloques correspondientes
    sub = x % 3

    if sub == 1:
        #a=a
        x = beta*x
        b = (b + 1) % (p-1)

    if sub == 0:
        x = (x * x) % p
        a = (2 * a) % (p-1)
        b = (2 * b) % (p-1)

    if sub == 2:
        x = (alpha * x) % p
        a = (a+1) % (p-1)
        #b = b

    return x,a,b



print("Solucion: ",Pollard(853,9,804,71))


