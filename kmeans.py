import random 
import numpy as np
from sklearn import datasets

def K_means (K, X, N) :
    m = len (X)

    rand = random.sample(range(m), K)

    cluster = dict()
    cluster.fromkeys(range(0,K))

    for i in range(0,K) :
        cluster[i] = [X[rand[i]], 0]

    c_x = dict()
    c_x.fromkeys(range(0,m))

    for iteration in range(0,N):
        for i in range(0,m) :
            dist = [np.linalg.norm(X[i] - cluster [j][0], 2) for j in range(0,K)]
            c_x[i] = np.argmin(dist)
        
        cluster_tmp = None
        coord_temp = [[np.zeros(len(X[0])), 0] for _ in range(0,K)]
    
        for i in range(0,m) :
            coord_temp[c_x[i]][0] +=X[i]
            coord_temp[c_x[i]][1] += 1
        for i in range(0,K) :
            sumatoria_coord = coord_temp[i][0]
            cont = coord_temp[i][1]
            cluster[i] = [sumatoria_coord / cont, cont] 

        if cluster_tmp == cluster:
            break
        cluster_tmp = cluster
    return c_x, cluster

if __name__ == '__main__':
    np.random.seed(5)
    
    vino = datasets.load_wine()
    X = vino.data
    K = int(input("Valor de K: "))
    N = int(input("Iteraciones N: "))

    c_x, cluster = K_means(K, X, N)

    print("Resultados: ", cluster)