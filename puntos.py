import matplotlib.pyplot as plt

class Punto:
    """ Clase que permite manejar un punto geometrico. Tiene las operaciones de Suma y Resta además de que tiene implementados la jerarquía y el string """
    
    def __init__(self, valores=[]):
        """ Constructor de la clase que toma como parametro una serie de valores, se usa por valor por defecto una lista vacia """
        self.valores = valores[:]

    def __add__(self, punto):
        """ sobrecarga del operador + """
        suma = [x+y for x,y in zip(self.valores, punto.valores)]
        return Punto(suma)

    def __sub__(self, punto):
        """ sobrecarga del operador - """
        resta = [x-y for x,y in zip(self.valores, punto.valores)]
        return Punto(resta)
    
    def __lt__(self, punto):
        """ sobrecarga del operador < """
        smag = sum([x**2 for x in self.valores])**0.5
        pmag = sum([x**2 for x in punto.valores])**0.5
        return smag < pmag
    
    def __str__(self):
        return ",".join(str(x) for x in self.valores)

if __name__=="__main__":
    puntos = []
    puntos.append(Punto([0,2]))
    puntos.append(Punto([-2,4]))
    puntos.append(Punto([5,10]))
    puntos.append(Punto([0,0]))
    puntos.append(Punto([-5,-10]))

    print("\n".join(str(punto) for punto in puntos))
    print("-"*30)
    print("\n".join(str(punto) for punto in sorted(puntos)))

    # se extraen los valores de X y Y de cada uno de los puntos de la lista puntos para ser graficados
    val_x = [punto.valores[0] for punto in puntos]
    val_y = [punto.valores[1] for punto in puntos]

    # se genera una grafica con cada uno de los puntos de la lista puntos, se usan las listas con los valores de X y Y debido a que este metodo pide dos listas uno con los valores de cada uno de los puntos en X y otro con cada uno de los puntos en Y
    plt.scatter(val_x, val_y, color="red")
    
    # se grafican los ejes de X y Y, desde -10 a 10 tanto para X como para Y
    plt.plot([-10,10],[0,0], color="black")
    plt.plot([0,0],[-10,10], color="black")
    
    # se muestra el gráfico generado
    plt.show()