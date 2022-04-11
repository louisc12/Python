import math
import random as ran
import numpy as np

def crearCromosoma(tamaño):
    individuo = [ran.randint(0,255) for i in range(tamaño)]
    return individuo 

def crearPoblacion(num,tamaño):
    poblacion = [ crearCromosoma(tamaño) for x in range(num)]
    return poblacion

def gramatica(individuo):
    expresion = []
    non_terminales = ['(','expre',')','op','pre-op','var'] #5
    variable = ['1','X'] #0
    operaciones = ['+','-','/','*']#3
    funciones= ['math.sqrt(','math.exp(','math.cos(','math.sin(','math.log('] #5

    if individuo[0] % 4 == 0:
        expresion.append(non_terminales[1])
        expresion.append(non_terminales[3])
        expresion.append(non_terminales[1])
    elif individuo[0] % 4 == 1:
        expresion.append(non_terminales[0])
        expresion.append(non_terminales[1])
        expresion.append(non_terminales[3])
        expresion.append(non_terminales[1])
        expresion.append(non_terminales[2])
    elif individuo[0] % 4 == 2:
        expresion.append(non_terminales[4])
        expresion.append(non_terminales[1]) 
    elif individuo[0] % 4 == 3:
        expresion.append(non_terminales[5]) 

    for j in range(1,tamaño):
        num = individuo[j] 
        for i in range(len(expresion)):
            if expresion[i] == 'op':
                valor = num & 3
                if valor == 0:
                    expresion[i] = operaciones[0]
                elif valor == 1:
                    expresion[i] = operaciones[1]
                elif valor == 2:
                    expresion[i] = operaciones[2]
                elif valor == 3:
                    expresion[i] = operaciones[3]
            if expresion[i]== 'pre-op':
                valor = num % 5
                if valor == 0:
                    expresion[i] = funciones[0]
                    expresion.append(')')
                elif valor == 1:
                    expresion[i] = funciones[1]
                    expresion.append(')')
                elif valor == 2:
                    expresion[i] = funciones[2]
                    expresion.append(')')
                elif valor == 3:
                    expresion[i] = funciones[3]
                    expresion.append(')')
                elif valor == 4:
                    expresion[i] = funciones[4]
                    expresion.append(')')
            if expresion[i]== 'var':
                valor = num & 1
                if valor == 0:
                    expresion[i] = variable[0]
                elif valor ==1:
                    expresion[i] = variable[1]
            if expresion[i] == 'expre':
                valor = num & 3
                if valor == 0:
                    expresion[i] = non_terminales[1]
                    expresion.insert(i+1,non_terminales[3]) 
                    expresion.insert(i+2,non_terminales[1])
                elif valor == 1:
                    expresion[i] = non_terminales[0]
                    expresion.insert(i+1,non_terminales[1]) 
                    expresion.insert(i+2,non_terminales[3])
                    expresion.insert(i+3,non_terminales[1])
                    expresion.insert(i+4,non_terminales[2]) 
                elif valor == 2:
                    expresion[i] = non_terminales[4]
                    expresion.insert(i+1,non_terminales[1])
                elif valor == 3:
                    expresion[i] = non_terminales[5]
                break

    funcion = ''.join(expresion)
    return funcion

def ECM(funcion,valorX,valorY,num):
    val = 0
    for i in range(len(valorX)):
        X = valorX[i]
        y= valorY[i]
        apt = eval(funcion)
        var = pow(apt - y,2)
        val += var
    val2 = math.sqrt(val/num)
    return val2

def leerArchivo():
    dataX=[]
    dataY=[]
    with open('/Users/louiscarrillo/Desktop/funcion.csv','r') as archivo:
        lineas = archivo.read().splitlines()
        lineas.pop(0)
        for l in lineas:
            linea = l.split(',')
            dataX.append(float(linea[0]))
            dataY.append(float(linea[1]))
    return dataX, dataY


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
    punto=ran.randint(1,len(poblacion[1]))
    cuarto = round(len(poblacion)/4)
    orden = sorted(poblacion,key=lambda x: x[-1])
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
    return nueva_poblacion

def cruzamiento2punto(poblacion):
    nueva_poblacion=[]
    punto1 = ran.randint(1,len(poblacion[1]))
    punto2 = ran.randint(punto1,len(poblacion[1]))

    for i in range(len(poblacion)):
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


def mutacion(poblacion,maximo=255):
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        punto1 = ran.randint(0,tamaño-2)
        poblacion[i][punto1] = np.random.randint(0,maximo+1)
        punto2 = ran.randint(0,tamaño-2)
        poblacion[i][punto2] = np.random.randint(0,maximo+1)
    for valor in poblacion:
        del(valor[-1])
    return poblacion

def mutacionFirst(poblacion):
    for i in range(len(poblacion)):
        tamaño=len(poblacion[i])
        punto1 = ran.randint(0,tamaño-2)
        poblacion[i][punto1] = np.random.randint(0,255)
        punto2 = ran.randint(0,tamaño-2)
        poblacion[i][punto2] = np.random.randint(0,255)
    poblacion[0][0] = np.random.randint(0,255)
    poblacion[0][1] = np.random.randint(0,255)
    poblacion[0][2] = np.random.randint(0,255)
    poblacion[0][3] = np.random.randint(0,255)
    for valor in poblacion:
        del(valor[-1])
    return poblacion

if __name__=="__main__":
    tamaño = 100
    num_poblacion=150000
    nueva_poblacion = []
    generaciones = 10000
    mejor=None

    poblacion = crearPoblacion(num_poblacion,tamaño)
    dataX,dataY = leerArchivo()

    for i in range(len(poblacion)):
        try:
            funcion = gramatica(poblacion[i])
            apt = ECM(funcion,dataX,dataY,len(dataX))
            poblacion[i].append(apt)
        except:
            poblacion[i].append(1000000000000000)

    for i in range(generaciones):
        try:
            seleccionados = seleccionRank(poblacion,50)
            cruzados = cruzamiento2punto(seleccionados)
            mutados = mutacion(cruzados)
            for x in mutados:
                g = gramatica(x)
                aptitud = ECM(g,dataX,dataY,len(dataX))
                x.append(aptitud)
            orden= sorted(poblacion,key=lambda x: x[-1])
            if mejor == None:
                mejor = orden[0]
            elif mejor != None:
                if orden[0][-1] < mejor[-1]:
                    mejor = orden[0]
                
            #print(f'Mejor solucion: {mejor} con gramatica: {gramatica(mejor)} en la generacion: {i}')
            #print('----'*25)
            poblacion = mutados
        except:
            pass
    try:
        print(mejor)
        print(gramatica(mejor))
    except:
        print(poblacion[0])
        print(gramatica(poblacion[0]))