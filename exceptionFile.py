if __name__=="__main__":
    try:
        archivo = open("ejemplo.txt","w")
        archivo.write("Ejemplo de escritura en archivo")
        archivo.write("Linea 2 del archivo ejemplo")
        archivo.write("ultima linea del archivo")
        archivo.close()

        with open("ejemplo.txt","r") as fp:
            print(" ".join(x.replace(" ","") for x in fp))
    except:
        pass    