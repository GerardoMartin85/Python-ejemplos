""" Script que automaticamente obtiene el premio del Euromillon y lo compara con el del usuario indicando resultado y premio/s, elaborado por Gerardo Martín, Julio 2020, obtiene los datos desde https://www.euromillones.com.es/ """
# coding: utf-8
import re
import time
from bs4 import BeautifulSoup
import requests              
#import urllib.request      


########## VARIABLES ##########
numerosJugados=[]  # Variables que almacena los números jugados
estrellasJugadas=[]          # Variables que almacena las estrellas jugadas
millonJugado="BWF61881"         # Variables que almacena el millon jugado

url=""
resultado=[]

combinacionGanadora=[]
estrellasganadoras=[]
millonganador=[]
fecha=[]
sdfsf


########## CÓDIGO ##########
if len(numerosJugados)==0:   # Aquí se entra solamente si no está rellena la variable numerosJugados
    try:
        while len(numerosJugados)<=4:
            entrada=int(input("Introduce uno a uno los numeros que juegas: "))
            numerosJugados.append(entrada)
        while len(estrellasJugadas)<=1:
            entrada=input("Introduce una a una las estrellas que juegas: ")
            estrellasJugadas.append(int(entrada))
    except:
        print("Debe de ser un numero.")


class web:    
    """ Se han separado cada elemento a buscar dependiendo de su nombre de clase en la web, cada elemento una vez limpiado con re es guardado en su lista correspondiente
    y comparado con su variable de elemento jugada correspondiente """
    

    def __init__(self,url):
        self.url=requests.get(url)
        self.data=self.url.text
        self.soup=BeautifulSoup(self.data,features="html.parser")


    def limpiaHtml(self,link):
        """Función que por parametro admite una variable que será limpiada de código de HTML <>/..."""
        self.resultado=re.sub(r"<.*?>","",str(link))
        return resultado


    def escaneoCombinacionGanadora(self):
        """ Este método se usa para obtener los 5 números ganadores desde la web, se obtienen en base a su nombre de clase, se le elimiman caracteres tipicos de HTML,
        y se añade a la lista correspondiente para luego en otro método ser comparada con los numeros jugados por el usuario """
        for link in self.soup.find_all(class_="numeros"):
            resultado=self.limpiaHtml(link)
            combinacionGanadora.append(int(self.resultado))
            

    def estrellas(self): # OJO esta función devuelve una lista y en la función print seleccionamos el index 3
       for link in self.soup.find_all(class_="estrellas"):
            resultado=self.limpiaHtml(link)  
            estrellasganadoras.append(int(self.resultado))
            

    def millon(self):
        for link in self.soup.find_all("span"):
            resultado=self.limpiaHtml(link)
            millonganador.append(self.resultado)
            
            
    def fechaSorteo(self):
        for link in self.soup.find("h4"):
            self.limpiado=re.sub(r"<.*?>","",str(link))
            fecha.append(self.limpiado) 
    

    def calculos(self):
        self.numerosComparados=set(combinacionGanadora) & set(numerosJugados)    # Comparación de ambas variables buscando coincidencias
        self.estrellasComparadas=set(estrellasganadoras) & set(estrellasJugadas) # Comparación de ambas variables buscando coincidencias


    def comprobar_premio(self):
        print("###########################################################################")
        print("Sorteo celebrado el dia:",fecha[1])
        print("Los numeros ganadores han sido:",combinacionGanadora)
        print("Los numeros jugados han sido:  ",numerosJugados)
        print("RESULTADOS COINCIDENTES:",self.numerosComparados)  
        print("")
        print("Las estrellas ganadoras han sido:",estrellasganadoras)
        print("Las estrellas jugadas han sido:  ",estrellasJugadas)
        print("RESULTADOS COINCIDENTES:",self.estrellasComparadas)
        print("")
        print("El millon ganador ha sido:",millonganador[3])
        print("El millon jugado ha sido: ",millonJugado)
        if millonganador == millonJugado:
        	print('¡¡ HAS ACERTADO EL MILLON. !!')
        else:
        	print('NO HAS ACERTADO EL MILLON.')
       
        print("")
        print("")
        print("Has tenido",len(self.numerosComparados),"numeros iguales y",len(self.estrellasComparadas),"estrellas iguales.")
        print("###########################################################################")


    def registrar(self):
        texto=("###########################\nRESULTADO DIA: "+fecha[1]+"\nNumeros ganadores: "+str(combinacionGanadora)+" Numeros jugados:"+str(numerosJugados)+"\nACIERTOS: "+str(self.numerosComparados)+
        "\nEstrellas ganadoras: "+str(estrellasganadoras)+" Estrellas jugadas: "+str(estrellasJugadas)+
        "\nMillon ganador: "+millonganador[3]+" Millon jugado: "+millonJugado+"\n##################\n")   
        registro=open("/volume1/Software/Mis aplicaciones/PYTHON Script Euromillones/resultados.txt","a") # Ruta por defecto del NAS: /volume1/Software/Mis aplicaciones/PYTHON Script Euromillones/resultados.txt
        registro.write(texto)
        registro.close()
        
    
    def __del__(self): # Destructor de clase
        print('Limpiando memoria...')

    

euromillon=web("https://www.euromillones.com.es/")
euromillon.escaneoCombinacionGanadora()
euromillon.estrellas()
euromillon.millon()
euromillon.fechaSorteo()
euromillon.calculos()
euromillon.comprobar_premio()
euromillon.registrar()
del euromillon
