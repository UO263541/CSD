import sys
import math


################### funciones anexas#####################

def es_primo(x):
  for d in range(2, math.floor(math.sqrt(x))+1):
    if(x%d == 0):
      return d
  return 0

def factorizar(n,base):
    ## Esta funcion devuelve los primos que lo componen para la base, con matices (los desechables por no  poder ser factorizados)
    # Presenta algunos errores
    #numeros_primos = iter((2, 3, 5, 7, 13))
    numeros_primos = iter(base)
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if n % numero_primo_actual != 0:
            # No se puede dividir por este número primo,
            # obtener el siguiente y volver a ejecutar
            # el bucle.
            try:
                numero_primo_actual = next(numeros_primos)
            except StopIteration:
                n=int(n)
                resultado.append(n)
                return resultado
            continue
        resultado.append(numero_primo_actual)
        n = cociente = n / numero_primo_actual
    return resultado





def conservar(lista, base):
    for i in lista:
        cond = i in base
        if (not cond):
            return False
    return True

#######CREAMOS CONSERVAR 2



def crearFila(neg,factbase, base):
    #Crea las filas teniendo en cuenta la base y añadiendo el -1 previamente si fuese necesario
    matriz=[]
    matriz.append(neg)
    num= len(base)
    for i in range (0,num):
        index = 0


        for j in factbase:
            if base[i]==j:
                index+=1
        matriz.append(index)

    return matriz


def transpose(matrix):
#transpose matrix so columns become rows, makes list comp easier to work with
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return(new_matrix)


def matrix(n):
    #Te devuelve una matriz con los posibles vectores de elección para una longitud determinada
    if n==0:
        return [[]]
    else:
       m = matrix(n-1)
       return [[i]+item for i in (0,1) for item in m]


def purgarmatriz(m):
    #Solamente que las sumas sean de maximo de tres vectores
    mP = []
    for i in m:
        if sum(i)>=1:
            mP.append(i)
    return mP


def seleccionarDeMatriz(vector, M):
    Mfinal = []
    for i in range(0,len(vector)):
        valor = vector[i]
        if valor!=0:
            Mfinal.append(M[i])
    return Mfinal


def suficientesValores(m):
    if len(m)==0:
        return False

    if len(m)==1:
        cont = 0
        lengVec = len(m[0])
        for i in m[0]:
            if i %2 ==0:
                cont +=1

        if cont == lengVec:
            return m
        else:
            return False


    else:
        longitud = len(m)  ## de cuantos elementos consta la matriz
        longVec = len(m[0]) ## tamaño de los vectores
        cont = 0
        matrizT = transpose(m) # matriz traspuesta para calcular las filas
        for i in matrizT:
            fila = sum(i)
            if fila%2==0:
                cont+=1

        if cont==longVec:
            return m

        else:
            matrizPosibilidades = matrix(longitud)
            matrizPosibilidades = purgarmatriz(matrizPosibilidades)

        # Bucle infinito a ver como se puede solucionar
            for i in matrizPosibilidades:
                m1 = seleccionarDeMatriz(i, m)
                booleano = suficientesValoresAUX(m1)
                if booleano:  # si en este caso es True
                    return booleano

        #No hay valores pues
        return False



def suficientesValoresAUX(m):
    if len(m)==0:
        return False

    if len(m)==1:
        cont = 0
        lengVec = len(m[0])
        for i in m[0]:
            if i %2 ==0:
                cont +=1

        if cont == lengVec:
            return m
        else:
            return False


    else:
        #Minimo hay dos vectores
        longitud = len(m)  ## de cuantos elementos consta la matriz
        longVec = len(m[0])  ## tamaño de los vectores
        cont = 0
        matrizT = transpose(m)  # matriz traspuesta para calcular las filas,
        for i in matrizT:
            fila = sum(i)
            if fila % 2 == 0:
                cont += 1

        if cont == longVec:
            return m

        #La suma de los elem es par
        else:
            return False



def suficientesValoresCongruencia(condicionP1, diccionario, base, n):
    if condicionP1==False:
        return False

    if len(condicionP1)==0:
        return False

    if len(condicionP1)==1:
        # si se desease comprobar que tambien funciona con la suma de filas de filas
        # se puede descomentar el return False de la linea inferior, asi solo comprobará filas
        #return False
        condicionP1 = condicionP1[0]
        elem = str(condicionP1)
        vect = diccionario[elem]
        x = vect[0]
        for i in range(len(condicionP1)):
            condicionP1[i] = condicionP1[i]/2
            condicionP1[i] = int(condicionP1[i])

        sumay = 1
        for i in range(len(condicionP1)):
            valor = int(math.pow(base[i], condicionP1[i]))
            sumay = sumay * valor

        y = sumay%n
        if (x == sumay or x == (sumay * -1) or x == y or x == (y * -1)):
            return False  # Hay que seguir iterando
        solucion = math.gcd(x - y, n)
        return solucion

    #### Mas de un elem la solucion
    As = []
    Bs = []
    sumaVect = []
    condicionParadaT = transpose(condicionP1)
    for i in condicionP1:
        elem = str(i)
        vect = diccionario[elem]
        valorA = vect[0]
        valorB = vect[1]
        As.append(valorA)
        Bs.append(valorB)

    x = 1
    for i in As:
        x = x * i
    xCong = x
    x = x % n

    for i in condicionParadaT:
        valor = sum(i)
        sumaVect.append(valor)

    sumaY = 1
    for i in range(len(sumaVect)):
        plus = sumaVect[i]
        valor = plus / 2
        valor = int(math.pow(base[i], valor))
        sumaY = sumaY * valor

    y = sumaY % n


    if (x==sumaY or x == (sumaY*-1) or x == y or x == (y*-1)):
        return False #Hay que seguir iterando

    solucion = math.gcd(x - y, n)


    return solucion




#Requiere un número entero positivo compuesto n
#Aseguro un factor de n
#B base de primos pequeños con -1
def cribaCuadratica(n,base):
    B = base
    b = B[1:len(B)]
    #print(b)
    m = math.sqrt(n)
    m = int(m) #redondeo por truncamiento
    i = 1
    t=0

    ###### Caso base o inicial#####
    ai = m+t #m
    bi0 = (ai * ai) - n
    neg = 0
    if (bi0 < 0):
        bi = bi0 * (-1)
        neg = 1
    else:
        bi = bi0
        neg = 0

    fbase = factorizar(bi, b)
    fila = crearFila(neg, fbase, b)
    neg = 0
    matrizA = [] #### 102
    matrizV = [] #### matriz a recorrer, key del diccionario
    matrizB = [] ####-175

    diccionario = {}
    if conservar(fbase,b):
        matrizA.append(ai)
        matrizB.append(bi0)
        matrizV.append(fila)
        vect = [ai,bi0]
        fila = str(fila)
        diccionario[fila]=vect


    condicionParada = suficientesValores(matrizV)
    condicionParada2 = suficientesValoresCongruencia(condicionParada, diccionario, base,n)


    #finalizamos caso base
    while((not condicionParada) or (not condicionParada2)):
        t+=1

        #Ejecucion positiva t positivo
        ##############################
        ai=m+t
        bi0=(ai * ai) - n
        if (bi0 < 0):
            bi = bi0 * (-1)
            neg = 1
        else:
            bi = bi0
            neg = 0

        #print("bi:",bi)
        fbase = factorizar(bi, b)
        #print("fbase pos:",fbase)

        if conservar(fbase,b): #Es factorizable? deberes: comprobar si mete el negativo
            fila = crearFila(neg, fbase, b)
            matrizA.append(ai)
            matrizB.append(bi0)
            matrizV.append(fila)
            vect = [ai, bi0]
            fila = str(fila)
            diccionario[fila] = vect
        #print("bi0:",bi0)


        condicionParada = suficientesValores(matrizV)
        condicionParada2 = suficientesValoresCongruencia(condicionParada, diccionario, base, n)
        if (condicionParada and condicionParada2):
            #SI hay condicionParada1 y 2
            return condicionParada2


        # Ejecucion negativa -> t negativo
        ai = m - t
        bi0 = ((ai) * (ai)) - n

        if (bi0 < 0):
            bi = bi0 * (-1)
            neg = 1
        else:
            bi = bi0
            neg = 0

        fbase = factorizar(bi, b)
        if conservar(fbase, b):  # Es factorizable? deberes: comprobar si mete el negativo
            fila = crearFila(neg, fbase, b)
            matrizA.append(ai)
            matrizB.append(bi0)
            matrizV.append(fila)
            vect = [ai, bi0]
            fila = str(fila)
            diccionario[fila] = vect

        condicionParada = suficientesValores(matrizV)
        condicionParada2 = suficientesValoresCongruencia(condicionParada, diccionario, base, n)
        if (condicionParada and condicionParada2):
            # SI hay condicionParada1 y 2
            return condicionParada2




    return condicionParada2




base = [-1,2,3,5,7,11,13]
sol = cribaCuadratica(10579,[-1,2,3,5,7,13])
print("SOLUCION: ",sol)










###### FUNCIONES OBSOLETAS##########

def factorizar2(numero, base):
 ## Esta funcion devuelve los primos que lo componen para la base, con matices (los desechables por no  poder ser factorizados)
 # Presenta algunos errores

 num_ini = numero
 num = num_ini
 num_fact = ''
 primos = base
 # Con primos = [1,2] tambien funcionaria
 seguir = True
 num_fact = []
 while seguir:
  if num ==1: # Se acabo la descomposicion
   break
  #print 'iteracion', primos[-1]
  for primo in primos[1:]:
   if num%primo == 0: # Si es divisible
    num = num/primo
    num_fact.append(primo)
  break # Saltamos el for
 return num_fact



def suficientesvaloresFALLO(m):
    #Caso base: 1 fila de matriz
    if len(m)==1:

        #for i in m: esto es por si hubiese varias filas
        cont=0 #contador de pares
        for j in m: #recorremos valores de la fila
            if (j%2)==0:
                cont+=1

        if cont==len(m):
            return True #nos vale la fila porque son todas pares
        else:
            return False #no nos vale


    #Caso base: 2 filas de matriz
    elif len(m)==2:
        condA = suficientesvaloresFALLO(m[0])
        condB = suficientesvaloresFALLO([m[1]])

        if condB or condA:
            return True


        cont = 0
        for j in range(len(m[0])):
            a = m[0][j]
            b = m[1][j]
            sum = a+b
            if (sum%2)==0:
                cont+=1
        if cont == len(m[0]):
            return True
        else:
            return False


    #Caso base len de m = 3
    elif len(m)==3:
        condA = suficientesvaloresFALLO(m[0])
        condB = suficientesvaloresFALLO([m[1]])
        condC = suficientesvaloresFALLO([m[2]])
        mA = m[0]
        mB = m[1]
        mC = m[2]
        mAB = [mA,mB]
        mAC = [mA,mC]
        mBC = [mB,mC]
        condAB = suficientesvaloresFALLO(mAB)
        condAC = suficientesvaloresFALLO(mAC)
        condBC = suficientesvaloresFALLO(mBC)

        vbool = [condA,condB,condC,condAB,condAC,condBC]

        if True in vbool:
            return True

        cont = 0
        for j in range(len(m[0])):
            a = m[0][j]
            b = m[1][j]
            c = m[2][j]
            sum = a + b + c
            if (sum % 2) == 0:
                cont += 1
        if cont == len(m[0]):
            return True
        else:
            return False
    return False
