# Creamos un modulo con las funciones
import statistics

def menor(lista):       # PAra saber si es menor
    m = lista[0]
    for n in lista:
        if  n < m :
            m = n
    return m

def mayor(lista):       # PAra saber si es mayor 
    m = lista[0]
    for n in lista:
        if  n > m :
            m = n
    return m

def promedio(lista):    #Pal promedio
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def suma(lista):        #Parar sumar 
    s = 0
    for n in lista:
        s += n
    return s

def leer():             # Ciclo para pedir e ingresar los numeros
    datos=[]
    while True:
        d=int(input("Ingresa un numero: "))
        if d==-1:
            break
        datos.append(d)
    return datos

def sumadigitos(lista):    #Parar sumar digitos individualmente  
    suma=0
    while lista!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

def recSumDat(lista):      #Parar sumar digitos individualmente y asignarlos a una lista
    rsd = []
    for n in lista:
        suma = 0
        while n!=0:
            dig = n % 10
            suma = suma + dig
            n = n // 10
        rsd.append(suma)
    return rsd

def factorial(lista):       #Parar sacar el factorial asignarlos a una lista
    fac = []
    for n in lista:
        f = 1
        for n in range(1, n+1):
            f = f * n
        fac.append(f)
    return fac

def media(lista):           #Parar sacar la media asignarlos a una lista
    s = 0
    for n in lista:
        s += n
    s = s/len(lista)
    return s

def varianza(lista):
    var = statistics.pvariance(lista)
    return var

def desviacion(lista):
    des = statistics.pstdev(lista)
    return des
