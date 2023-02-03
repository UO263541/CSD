import sys
import math
import hashlib







def Yuval(m):
    #Require: Par de mensajes legítimo e ilegítimo: xl,xil
    #Require: Función hash h de m bits

    t = math.pow(2,m/2)
    t = int(t)

    msgLegit = [
        ["Buenos días", "Buenas tardes"],
        ["mi nombre es Jose", "mi nombre es Jose,"],
        ["le comunico", "le esta siendo notificado"],
        ["que ha sido seleccionado", "que ha sido escogido"],
        ["para una cena exclusiva", "para una comida exclusiva"],
        ["en el Hotel Palace", "En el hotel Miracle"],
        ["por cortesia", "por gran cortesía"],
        ["del excelentísimo", "del magnífico"],
        ["anfitrión", "anfitrión,"],
        ["el señor", "don"],
        ["Donato", "Severino"],
        ["rector de la UPV.", "rector de la UV."],
        ["El motivo", "La principal razón"],
        ["de su elección", "de su escogimiento"],
        ["ha sido", "claramente ha sido"],
        ["su magnífica tesis", "su excelente tesis"],
        ["sobre", "referente a"],
        ["la Factorización de enteros.", "el calculo del Logaritmo Discreto."],
        ["En consecuencia", "En consecuencia,"],
        ["le esperamos", "contamos con usted"]
    ]
    msgIlegit = [
        ["Buenos noches", "Buenas noches,"],
        ["mi nombre es Osama", "mi nombre es Bin Laden,"],
        ["se le comunica", "se le notifica"],
        ["que ha sido tristemente seleccionado", "que ha sido tristemente escogido"],
        ["para una paliza exclusiva", "para una tortura exclusiva"],
        ["en Arabia", "en Catar"],
        ["por cortesia", "por gran cortesía"],
        ["del excelentísimo", "del magnífico"],
        ["anfitrión", "anfitrión,"],
        ["Lord", "Lords"],
        ["Antonio Garabito", "Alfredo Garabito"],
        ["sicario profesional.", "asesino en serie profesional."],
        ["El principal motivo", "La razón"],
        ["de su elección", "de su escogimiento"],
        ["ha sido", "claramente ha sido"],
        ["su esperpéntica tesis", "su excretable tesis"],
        ["sobre", "referente a"],
        ["la Factorización de enteros.", "el calculo del Logaritmo Discreto."],
        ["En consecuencia", "En consecuencia,"],
        ["iremos por usted.", "vamos por usted."]
    ]

    dicLegal = dict()#diccionario hash Legal, mensaje legal
    dicIlegal = dict()

    for i in range(t):
        decimal = i
        cadenaHash = ""
        cadenaHashIlegitimo = ""
        modulos = [] # la lista para guardar los módulos


        while decimal != 0:  # mientras el número de entrada sea diferente de cero
            # paso 1: dividimos entre 2
            modulo = decimal % 2
            cociente = decimal // 2
            modulos.append(modulo)  # guardamos el módulo calculado
            decimal = cociente  # el cociente pasa a ser el número de entrada


        while (len(modulos)< (m/2)):
            modulos.append(0)
        modulos = list(reversed(modulos))


        for i in range (len(modulos)):
            valor = modulos[i] #0 o 1
            sL = msgLegit[i]
            sI = msgIlegit[i]
            cadLegal = sL[valor]
            cadIlegal = sI[valor]
            cadenaHash+=cadLegal+" "
            cadenaHashIlegitimo += cadIlegal + " "

        hashLegal = resumen(cadenaHash)
        hashIlegal = resumen(cadenaHashIlegitimo)

        dicLegal[hashLegal] = cadenaHash
        dicIlegal[hashIlegal] = cadenaHashIlegitimo

    ListaIHashes = list(dicIlegal.keys())
    ListaLHashes = list(dicLegal.keys())
    ListaLHashesColision = list(intersecion(ListaLHashes,ListaIHashes))


    print(ListaLHashesColision)


"""
    if (hashIlegal) in dicLegal.keys():
        print (hashIlegal,dicLegal[hashIlegal])
        print (cadenaHashIlegitimo)
        print (resumen(dicLegal[hashIlegal]))
        print (resumen(cadenaHashIlegitimo))
        #listaI.append(hashIlegal)
"""







    #print(dicLegal)



"""
        if "8a7163" in dicLegal.keys():
        print("paco")
        for i in listaI:
        print(i)
        if i in dicLegal.keys():
            print("colision")
"""




def resumen(m):

    h = hashlib.md5(m.encode())
    str = ""
    hasheao = h.hexdigest()

    for i in range(8): #32 bits
        v=hasheao[i]
        str+=v
    return str


def matrix(n):
    #Te devuelve una matriz con los posibles vectores de elección para una longitud determinada
    if n==0:
        return [[]]
    else:
       m = matrix(n-1)
       return [[i]+item for i in (0,1) for item in m]


def seleccionarDeMatriz(vector, M):
    Mfinal = []
    for i in range(0,len(vector)):
        valor = vector[i]
        if valor!=0:
            Mfinal.append(M[i])
    return Mfinal


def intersecion(l1, l2):
    return set(l1).intersection(l2)

Yuval(40)
#

# este programa extensivo nos devolvería un numero mayor que 15 de colisiones
#sha 32 bits???