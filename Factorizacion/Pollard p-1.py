import random
import sys
import math
import random
import numpy
import time
#Require: Un número entero positivo compuesto n
#Ensure factor de n

def PollardP(n):
    print("Entero positivo compuesto de entrada N:",n)
    A = random.randint(2,n-1)
    A = int(A)
    mcd = math.gcd(A,n)
    if (1<mcd and mcd < n):
        return mcd
    k=2
    while True:
        A = (pow(A,k,n))
        A = int(A)
        d = math.gcd(A-1,n)
        if (1<d and d<n):
            return d
        if d==n:
            return False
        k+=1


start = time.time()


print("Solucion: ",PollardP(63897587222538985880186825791))

end = time.time()
print("Tiempo: ",end-start)