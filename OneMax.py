import numpy as np
import random as ran
import math

def crearCromosoma(tamaño):
    individuo = [ran.randint(0,1) for i in range(tamaño)]
    return individuo

def fitness(cromosona):
    return sum(cromosona)

def seleccion(poblacion,tamaño,seleccion,num=4):
    seleccionados=[]
    for j in range(seleccion):
        for i in range(num):
            torneo=[]
            torneo.append(poblacion[ran.randint(0,tamaño-1)])
        temp = sorted(torneo,key=lambda x: x[-1])
        seleccionados.append(temp[-1])
    return seleccionados

def cruzamiento(poblacion):
    nueva_poblacion=[]
    punto = ran.randint(3,len(poblacion[1]))

    for i in range(len(poblacion)):
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
    #for valor in poblacion:
        #valor.pop(-1)
        #nueva_poblacion.append(valor)
    for individuo in nueva_poblacion:
        del(individuo[-1])
    return nueva_poblacion

def mutacion(poblacion,tamaño):
    for i in range(len(poblacion)):
        posicion = ran.randint(0,tamaño-1)
        if poblacion[i][posicion] == 0:
            poblacion[i][posicion]=1
        elif poblacion[i][posicion] == 1:
            poblacion[i][posicion]=0
    #for valor in poblacion:
        #fit = fitness(valor)
        #valor.append(fit)
    return poblacion


if __name__=="__main__":
    poblacionActual=[]
    tamaño = 12
    num_individuos=15
    seleccionar = int(round(num_individuos/2))
    generaciones=5000
    mejor=None

    for i in range(num_individuos):
        individuo=crearCromosoma(tamaño)
        aptitud= fitness(individuo)
        individuo.append(aptitud)
        poblacionActual.append(individuo)
    
    for l in range(generaciones):
        poblacion = sorted(poblacionActual,key=lambda x: x[-1])
        #print(poblacion)
        #print("-----------------------------------------------")
        elegidos=seleccion(poblacion,num_individuos,seleccionar)
        #print(elegidos)
        cruza=cruzamiento(elegidos)
        #print("------------------------------------------------")
        #print(cruza)
        #print("--------------------------------------------------")
        mutar=mutacion(cruza,tamaño)
        #print("--------------------------------------------------")
        #print(mutar)
        #print("--------------------------------------------------")
        for x in mutar:
            fit = fitness(x)
            x.append(fit)
        #print(mutar)
        mutadosOrdenados = sorted(mutar,key=lambda x: x[-1])
        mejor=mutadosOrdenados[-1]
        #print("--------------------------------------------------")
        print(f' mejor solicion {mejor} de la generacion {l}')
        if mejor[-1]==tamaño:
            break
        else:
            poblacionActual = mutar
    