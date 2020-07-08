import os # Modulo de sistema para generar Función que permite borrar la consola

def Entrada():
    """Módulo que captura el número entero para realizar el rango en el juego, lo devuelve como numero
   """
    numero=input("Escribe un número para realizar el rango desde 0 al número que tú elijas: ")
    numero=int(numero)
    if numero>0:
    	os.system("cls") #Función que permite borrar la consola
    	print("El rango será desde 0 al {}.".format(numero))
    else:
        print("Error, debe de ser un número superior a cero, el programa se cerrará"),sys.exit(0)
    return numero
