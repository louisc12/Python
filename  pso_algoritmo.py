import numpy as np
import random as ran
import math


def crearParticula(tamaño):
    particula = [ran.randint(100,12000000) for i in range(tamaño)]
    return particula

def crearVelocidad(tamaño):
    particula = [0 for i in range(tamaño)]
    return particula

def crearPoblacion(tamaño,dimension):
    poblacion=[crearParticula(dimension) for x in range(tamaño)]
    return poblacion

def crearVelocidades(tamaño,dimension):
    poblacion=[crearVelocidad(dimension) for x in range(tamaño)]
    return poblacion

def FuncionObjetivoSphere(individuo):
    val =0
    for i in range(len(individuo)):
        val += individuo[i]**2
    return val

def FuncionObjetivo(individuo):
    val = 0
    val = (math.pi * (individuo[0]/2)**2) * individuo[1]
    return val

def UpdateVelocidad(x, v, l_best, g_best, c0=1.0, c1=1.0,w=0.75):
    alpha=[]
    beta=[]
    G=[]
    L=[]
    nueva_v=[]
    uv=[]
    ep1=[ran.uniform(0,1) for x in range(len(x))]
    ep2=[ran.uniform(0,1) for x in range(len(x))]
    for i in range(len(v)):
        vv = w * v[i]
        uv.append(vv)
    for i in range(len(x)):
        al = c0 * ep1[i]
        alpha.append(al)
        be = c1 * ep2[i]
        beta.append(be)
    for i in range(len(x)):
        posG = g_best[i] - x[i]
        G.append(posG)
        posL = l_best[i] - x[i]
        L.append(posL)
    for i in range(len(x)):
        nv = uv[i] + (alpha[i] * L[i]) + (beta[i] * G[i])
        nueva_v.append(nv)
    return nueva_v

def UpdatePosicion(x, v):
    nueva_posicion=[]
    for i in range(len(x)):
        new_x = x[i] + v[i]
        nueva_posicion.append(new_x)
    return nueva_posicion

if __name__=="__main__":
    Gbest=None
    dimension=3
    num_poblacion =150
    iteraciones = 100

    velocidades = crearVelocidades(num_poblacion,dimension)
    particulas = crearPoblacion(num_poblacion,dimension)

    for l in range(iteraciones):
        for i in range(len(particulas)):
            fit = FuncionObjetivoSphere(particulas[i])
            particulas[i].append(fit)
            

        orden= sorted(particulas,key=lambda x: x[-1])

        if Gbest == None:
            Gbest = orden[0]
        elif Gbest != None:
            if orden[0][-1] < FuncionObjetivoSphere(Gbest):
                Gbest = orden[0]
            else:
                pass
        for i in range(len(particulas)):
            particulas[i].pop(-1)

        for i in range(len(particulas)):
            v = UpdateVelocidad(particulas[i],velocidades[i],orden[0],Gbest)
            velocidades[i] = v

        for i in range(len(particulas)):
            p = UpdatePosicion(particulas[i],velocidades[i])
            particulas[i] = p
        #print(f'Mejor particula es: {Gbest,FuncionObjetivoSphere(Gbest)} en la iteracion {l}')
        #print(f'Mejor fitness es: {FuncionObjetivo(Gbest)} con las posiciones: {Gbest}')
        print(f'Mejor fitness es: {float(FuncionObjetivoSphere(Gbest))} en {l}')
        #print(f'Mejor fitness es: {Gbest}')
    print(f'Mejor fitness es: {float(FuncionObjetivoSphere(Gbest))} en {l} con {Gbest}')