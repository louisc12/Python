from multiprocessing import Pool

def valor_pi(inicio,fin,step):
    num=1
    for i in range(inicio, fin,step):
        numerador =(2 * i)**2
        denominador =((2 * i) - 1) * ((2 * i) + 1)
        resul = numerador/denominador
        num=num*resul
    return num
        
if __name__=="__main__":
    num_pi=2
    iteraciones=int(input("Ingrese un valor para iteraciones: "))
    hi=int(input("Ingrese un valor para los procesos: "))
    pool=Pool()

    Resultados = [pool.apply_async(valor_pi,args=(i,iteraciones,hi,) ) for i in range(1, hi+1)]
    pool.close()
    pool.join()

    lista_pi=[]
    for val in Resultados:
        num=val.get()
        lista_pi.append(num)
    
    for val in lista_pi:
        num_pi = num_pi*val
    print(num_pi)