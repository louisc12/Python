import numpy as np
import random as rand

#funcion de activacion
def escalon(x):
    if x > 0:
        return 1
    else:
        return 0

#funcion derivada
def escalon_derivada(x):
    return 1

def sumatoria(entradas,pesos,sesgo):
    return np.dot(entradas,pesos)+sesgo

def forward(X):
    return escalon(X)

def error(esperado,obtenido):
    return (esperado - obtenido)

def delta(error,Neta,x):
    return (error) * (escalon_derivada(Neta)) * (x)

def ajuste(lr,delta):
    valorAjuste = (lr) * (delta)
    return valorAjuste

if __name__=="__main__":
    entradas = [[0,0],[0,1],[1,0],[1,1]]

    salida = [0,0,0,1] 

    pesos =[rand.random() * (0.5+0.5) - 0.5 for x in range(len(entradas[0]))]

    sesgo = rand.random() * (0.5+0.5) - 0.5

    lr=0.15

    epocas=5

    #print(pesos)
    for l in range(epocas):
        for i in range(len(entradas)):
            #print('----------------------')
            valorSumatoria = sumatoria(entradas[i],pesos,sesgo)
            #print(f'valor de neto: {valorSumatoria}')
            valorSalida = forward(valorSumatoria)
            #print(f'valor de salida: {valorSalida}')
            valorError = error(salida[i],valorSalida)
            #print(f'valor de esperado: {salida[i]}')
            #print(f'valor de error: {valorError}')
            if salida[i] == valorSalida:
                pass
            else:
                for j in range(len(pesos)):
                    nuevoPeso = pesos[j] + (valorError * entradas[i][j])
                    pesos[j] = nuevoPeso
                    nuevoSesgo = sesgo + valorError
                    sesgo = nuevoSesgo
        #print(pesos)
    print(forward(sumatoria(entradas[3],pesos,sesgo)))