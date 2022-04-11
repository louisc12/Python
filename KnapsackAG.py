import numpy as np
import random as ran


def crearCromosoma(tamaño):
    individuo = [ran.randint(0,1) for i in range(tamaño)]
    return individuo

def Articulos(cromosona,Articulos):
    lista=[]
    for a,b in zip(cromosona,Articulos):
        if a==1:
            lista.append(b)
    return lista

def fitnessPeso(cromosona,pesos):
    peso=0
    for a,b in zip(cromosona,pesos):
        val = a*b
        peso = peso + val
    return peso

def fitnessValor(cromosona,valores):
    valor=0
    for a,b in zip(cromosona,valores):
        temp = a*b
        valor = valor + temp
    return valor


def seleccion(poblacion,tamaño,seleccion,num=4):
    seleccionados=[]
    for j in range(seleccion):
        for i in range(num):
            torneo=[]
            torneo.append(poblacion[ran.randint(0,tamaño-1)])
        temp = sorted(torneo,key=lambda x: x[-1])
        seleccionados.append(temp[-1])
    return seleccionados

def cruzamiento1punto(poblacion):
    nueva_poblacion=[]
    punto=11

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
    #for valor in poblacion:
        #valor.pop(-1)
        #nueva_poblacion.append(valor)
    ##for individuo in nueva_poblacion:
        #del(individuo[-1])
    return nueva_poblacion

def cruzamiento2punto(poblacion):
    nueva_poblacion=[]
    punto1 = 8
    punto2 = 16

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

def mutacion(poblacion):
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        posicion = ran.randint(0,tamaño-1)
        if poblacion[i][posicion] == 0:
            poblacion[i][posicion]=1
        elif poblacion[i][posicion] == 1:
            poblacion[i][posicion]=0
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        posicion = ran.randint(0,tamaño-1)
        if poblacion[i][posicion] == 0:
            poblacion[i][posicion]=1
        elif poblacion[i][posicion] == 1:
            poblacion[i][posicion]=0
    for valor in poblacion:
        del(valor[-1])
    return poblacion


if __name__=="__main__":
    poblacionActual=[]
    mejoresSoluciones=[]
    articulos=['Mapa','Brujula','Agua','Sandwich','Glucosa','Estaño','Banana','Manzana','Queso','Cerveza','Crema Bronceadora','Camara','Camisa','Pantalones','Paraguas','Pantalones aprueba de agua','abrigos contra agua','cartera','lentes','tualla','calcetas','libro']
    pesos=[9,13,153,50,15,68,27,39,23,52,11,32,24,48,73,42,43,22,7,18,4,30]
    valores=[150,35,200,160,60,45,60,40,30,10,70,30,15,10,40,70,75,80,20,12,50,10]
    tamaño = 22
    num_individuos=1000
    seleccionar = int(round(num_individuos/4))
    generaciones=10000


    for i in range(num_individuos):
        individuo=crearCromosoma(tamaño)
        w = fitnessPeso(individuo,pesos)
        apt = fitnessValor(individuo,valores)
        if w <= 400:
            individuo.append(apt)
            poblacionActual.append(individuo)

    for i in range(generaciones):
        temp=[]
        elegidos = seleccion(poblacionActual,len(poblacionActual[0]),seleccionar)
        
        cruza = cruzamiento1punto(elegidos)

        mutar = mutacion(cruza)
        
        for x in mutar:
            w = fitnessPeso(x,pesos)
            if w <= 400:
                v = fitnessValor(x,valores)
                x.append(v)
                temp.append(x)

        orden = sorted(temp,key=lambda x: x[-1])
        for x in orden:
            mejoresSoluciones.append(orden[-1])
        print(f'Mejor solucion de la generacion {i}: {orden[-1]}')
        poblacionActual=orden

    soluciones = sorted(mejoresSoluciones,key=lambda x: x[-1])
    
    print("---------------------------------")
    print(f'Mejor solucion: {soluciones[-1]}')
    items = Articulos(soluciones[-1],articulos)
    print(f'Articulos: {items}')
    w = fitnessPeso(soluciones[-1],pesos)
    print(f'Peso: {w}')
    v = fitnessValor(soluciones[-1],valores)
    print(f'valor: {v}')