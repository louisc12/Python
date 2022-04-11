  
def fibo(num):
   if num <= 1:
       return num
   else:
       return(fibo(num-1) + fibo(num-2))      
  
 
if __name__=="__main__":
    
    numero = int(input("elige el numero que deseas: "))
    if numero <= 0:
       print("mayor a 0")
    else:
       print("valores: ")
    for i in range(numero):
       print(fibo(i),end="-")  