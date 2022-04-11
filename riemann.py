
def sumatoria(ls=10,li=1,rectan=500):
    base = (ls-li)/rectan
    li=1
    sum=0
    for _ in range(rectan):
        res = (li**2)*base
        #print(res)
        li+=base
        sum +=res
    print(f'la suma de los valores es de {sum}')    


if __name__=="__main__":
    sumatoria()