import math
class punto2D:
    def __init__(self,X=0,Y=0):
        self.X=X
        self.Y=Y
    def cuadrante(self):
        if self.X==0 and self.Y!=0:
            return print("eje de las Y")    
        elif self.X!=0 and self.Y==0:
            return print("eje de las X")
        elif self.X==0 and self.Y==0:
            return print("esta en el origen (0,0)")
        elif self.X >0 and self.Y >0:
            return print("primer cuadrante positivo")
        elif self.X <0 and self.Y <0:
            return print("tercer cuadrante negativo")
        elif self.X <0 and self.Y >0:
            return print("segundo cuadrante positivo en y y negativo en x") 
        elif self.X >0 and self.Y <0:
            return print("cuarto cuadrante positivo en x y negativo en y")                                
    def __str__(self):
        return f'P(X:{self.X},Y:{self.Y})'
    def vector(self,punto2D):
        X=punto2D.X-self.X
        Y=punto2D.Y-self.X
        return(X,Y)
    def distancia(self,punto2D):
        distanc = math.sqrt((punto2D.X-self.X)**2+(punto2D.Y-self.Y)**2)
        return distanc

class rectangulo:
    def __init__(self, pInicial=punto2D(), pFinal=punto2D()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        self.vBase = abs(self.pFinal.X - self.pInicial.X)
        self.vAltura = abs(self.pFinal.Y - self.pInicial.Y)
        self.vArea = self.vBase * self.vAltura
    def base(self):
        print(f'El base del rectángulo es {self.vBase}')
    def altura(self):
        print(f'El altura del rectángulo es {self.vAltura}')
    def area(self):
        print(f'El área del rectángulo es {self.vArea}')

if __name__=="__main__":
    p1 = punto2D(2,6)
    p2 = punto2D(2,-7)
    p3 = punto2D(-1,6)
    p4 = punto2D(9,4)
    p5 = punto2D(0,0)
    print("-"*50)
    print("punto 1: ",p1)
    p1.cuadrante()
    print("punto 2: ",p2)
    p2.cuadrante()
    print("la distancia entre estos puntos es:",p1.distancia(p2))
    print("el vector entre los puntos es: ",p1.vector(p2))
    print("-"*50)
    print("punto 5: ",p5)
    p5.cuadrante()
    print("punto 3: ",p3)
    p3.cuadrante()
    print("vector entre los puntos es: ",p5.vector(p3))
    print("distancia: ",p5.distancia(p3))
    print("-"*50,"rectangulo")
    R = rectangulo(p1,p4)
    R.base()
    R.altura()
    R.area()