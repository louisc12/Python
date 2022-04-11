import numpy as np
import random as ran
import sys

def crearCromosoma(tamaño,maximo):
    individuo = [np.random.randint(1,maximo+1) for i in range(tamaño)]
    return individuo

def crearPoblacion(num,tamaño,maximo):
    poblacion = [ crearCromosoma(tamaño,maximo) for x in range(num)]
    return poblacion

def amenazas(individuo):
    amenazas=0
    for i in range(len(individuo)):
        actual = individuo[i]
        contador=1
        for j in range(i+1,len(individuo)):
            otro = individuo[j]
            if actual == otro or actual+contador == otro or actual-contador ==otro:
                amenazas=amenazas+1    
            contador = contador + 1 
    return amenazas

def seleccionTorneo(poblacion,tamaño,seleccion,num=4):
    seleccionados=[]
    for j in range(seleccion):
        for i in range(num):
            torneo=[]
            torneo.append(poblacion[ran.randint(0,tamaño-1)])
        temp = sorted(torneo,key=lambda x: x[-1])
        seleccionados.append(temp[0])
    return seleccionados

def seleccionRank(poblacion,seleccion=10):
    seleccionados=[]
    temp = sorted(poblacion,key=lambda x: x[-1])
    for j in range(seleccion):
        seleccionados.append(temp[j])
    return seleccionados

def cruzamiento1punto(poblacion):
    nueva_poblacion=[]
    punto=ran.randint(3,len(poblacion[1]))
    cuarto = round(len(poblacion)/4)
    orden = sorted(poblacion,key=lambda x: x[-1])
    for i in range(len(poblacion)):
        #del(poblacion[i][-1])
        padre=poblacion[i]
        num = ran.randint(0,len(poblacion)-1)
        if num !=i:
            madre=poblacion[num]
        else:
            while num == i:
                num = ran.randint(0,len(poblacion)-1)
            madre=poblacion[num]
        hijo1 = padre[:punto] + madre[punto:]
        hijo2 = madre[:punto] + padre[punto:]
        nueva_poblacion.append(hijo1)
        nueva_poblacion.append(hijo2)
    #for i in range(cuarto):
        #nueva_poblacion.append(orden[i])
        
    #for valor in poblacion:
        #valor.pop(-1)
        #nueva_poblacion.append(valor)
    ##for individuo in nueva_poblacion:
        #del(individuo[-1])
    return nueva_poblacion

def cruzamiento2punto(poblacion):
    nueva_poblacion=[]
    punto1 = ran.randint(3,len(poblacion[1]))
    punto2 = ran.randint(punto1,len(poblacion[1]))

    for i in range(len(poblacion)):
        #del(poblacion[i][-1])
        padre=poblacion[i]
        num = ran.randint(0,len(poblacion)-1)
        if num !=i:
            madre=poblacion[num]
        else:
            while num == i:
                num = ran.randint(0,len(poblacion)-1)
            madre=poblacion[num]
        hijo1 = padre[:punto1] + madre[punto1:punto2]+ padre[punto2:]
        hijo2 = madre[:punto1] + padre[punto1:punto2] + madre[punto2:]
        nueva_poblacion.append(hijo1)
        nueva_poblacion.append(hijo2)
    #for valor in poblacion:
        #valor.pop(-1)
        #nueva_poblacion.append(valor)
    ##for individuo in nueva_poblacion:
        #del(individuo[-1])
    return nueva_poblacion

def mutacionSwap(poblacion):
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        punto1 = ran.randint(0,tamaño-2)
        punto2 = ran.randint(0,tamaño-2)
        poblacion[i][punto1] = poblacion[i][punto2]
        poblacion[i][punto2] = poblacion[i][punto1]
    for valor in poblacion:
        del(valor[-1])
    return poblacion


def mutacion(poblacion,maximo):
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        punto1 = ran.randint(0,tamaño-2)
        poblacion[i][punto1] = np.random.randint(1,maximo+1)
    for valor in poblacion:
        del(valor[-1])
    return poblacion

if __name__=="__main__":
    tamaño = 8
    maximo = tamaño
    num=2000
    seleccionar= int(round(num/3))
    generaciones=10000

    poblacion = crearPoblacion(num,tamaño,maximo)
    #print(poblacion)
    for x in poblacion:
        apt = amenazas(x)
        x.append(apt)
        #print(apt)

    for i in range(generaciones):
        #selected = seleccionTorneo(poblacion,tamaño,seleccionar)
        selected = seleccionRank(poblacion,seleccionar)
        #print(selected)
        cruzados = cruzamiento2punto(selected)
        #print(cruzados)
        #mutados = mutacion(cruzados,maximo)
        mutados = mutacionSwap(cruzados)
        #print(mutados)
        for x in mutados:
            aptitud = amenazas(x)
            x.append(aptitud)
        orden = sorted(mutados,key=lambda x: x[-1])
        mejor = orden[0]
        print(f'Mejor : {mejor} en generacion {i}')
        if mejor[-1]==0:
            print(f'SOLUCION : {mejor}')
            break
        else:
            poblacionActual = mutados