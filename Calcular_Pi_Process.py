from multiprocessing import Process, Queue

def PI_Process(inicio,fin,step,queue):
    PI = 2
    for k in range(inicio, fin):

        val1=(2 * k)/((2 * k)+1)
        val2=(2 * k)/((2 * k)-1)
        valSuma=val1*val2
        PI *= valSuma
    queue.put(PI)


if __name__ == "__main__":
    
    n = int(input("Ingrese un valor para aplicar PI: "))
    nProc = int(input("Ingrese la cantidad procesos: ")) 
    ListaProcesos =[]

    queue =Queue()

    for i in range(1,nProc+1):
        ListaProcesos.append(Process(target=PI_Process, args=(i, n, nProc, queue,)))
        ListaProcesos[-1].start()

    for proceso in ListaProcesos:
        proceso.join()

    resultado=[]
    while not queue.empty():
        resultado.append(queue.get())

    print("Resultado Final: ",resultado[0])
    #nuevalista = list(resultado)
    #print(nuevalista)
    










