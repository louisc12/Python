import numpy as np 

#funcion de activacion
def sigmoid(x):
    return 1/(1+np.exp(-x))

#funcion derivada
def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

#funcion lineal
def function_h(X,W,b):
    return np.dot(W,X)+b

def output_y(X,W,b):
    return sigmoid(function_h(X,W,b))

def error_term(y,W,X,b):
    error = y - output_y(X,W,b)
    delta = error * sigmoid_prime(function_h(X,W,b))
    return delta

def increment(W,X,b,eta,i,y):
    incremento = eta * error_term(y,W,X,b) * X[i]
    return incremento

if __name__=="__main__":
    learning_rate = 0.5
    x = np.array([1,1])
    y = 5
    w = np.array([0.1,0.2])
    b = 0
    salida = output_y(x,w,b)
    print("Salida: ",salida)
    residual = y - salida
    print("Error",residual)
    incremento = [increment(w,x,b,learning_rate,0,y),increment(w,x,b,learning_rate,1,y)]
    print("incremento: ",incremento)
    n_w = w + incremento
    print("nuevos pesos: ",n_w)
    n_error= y - output_y(x,n_w,b)
    print("nuevo error: ",n_error)