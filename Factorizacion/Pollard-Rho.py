import random
import sys
import math
import random
import numpy
import time

#Require: Un número entero positivo compuesto n
#Ensure factor de n

def PollardRho2(n):
    #Sin Habitualmente
    A = random.randint(2,n-1)
    B=A
    while True:
        A = ((A * A) + 1) % n
        B = ((B * B) + 1) % n
        B = ((B * B) + 1) % n
        p = math.gcd(A - B, n)
        if (1 < p and p < n):
            return p
        if (p == n):
            return p

def PollardRho(n):
    #En este caso considerando que habitualmente A y B se toma el valor 2
    A=2
    B=2
    while True:

        A= ((A*A)+1)% n
        B = ((B * B) + 1) % n
        B = ((B * B) + 1) % n
        p = math.gcd(A-B,n)
        if (1<p and p<n):
            return p
        if (p==n):
            return False #Devuelve que el algoritmo no ha encontrado el factor



print (PollardRho(18446744073709551617))
start = time.time()
print(PollardRho(340282366920938463463374607431768211457))
end = time.time()
print("Tiempo: ",end-start)


v = [16223, 16229, 16231, 16249, 16253, 1626, 16273, 16301, 16319, 16333, 16339,
16349, 16361, 16363, 16369, 16381]



for i in v:
    print(PollardRho(i))


