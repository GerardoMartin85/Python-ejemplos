""" Script que automaticamente obtiene el premio del Euromillon y lo compara con el del usuario indicando resultado y premio/s, elaborado por Gerardo Martín, Julio 2020"""
# coding: utf-8
import re
import time
from bs4 import BeautifulSoup
import requests              
import time


########## VARIABLES ##########
numerosJugados=[17,20,22,41,50]  # Variable que almacena los números jugados 
estrellasJugadas=[1,9]           # Variable que almacena las estrellas jugadas
millonJugado=["CFB91606"]        # Variable que almacena el millon jugado  
url=""
combinacionGanadora=[]
estrellasganadoras=[]
millonganador=[]
fecha=[]


########## CÓDIGO ##########
if len(numerosJugados)==0:   # Aquí se entra solamente si no está rellena la variable numerosJugados
    while len(numerosJugados)<=4:
        try:
            entrada=int (input("Introduce uno de los numeros que juegas y pulsa intro: "))
            numerosJugados.append(entrada)
            while len(estrellasJugadas)<=1:
                entrada=input("Introduce una de las estrellas que juegas y pulsa intro: ")
                estrellasJugadas.append(int(entrada))
        except:
            print("Debe de ser un numero.")
    millonJugado=input("Introduce el codigo del millon jugado: ").upper()  
    


class web:    
    """ Se han separado cada elemento a buscar dependiendo de su nombre de clase en la web, cada elemento una vez limpiado con re es guardado en su lista correspondiente
    y comparado con su variable de elemento jugada correspondiente """
    def __init__(self,url):
        self.contador=0
        while self.contador<=5:
        	try:
        		self.url=requests.get(url)
        		self.data=self.url.text
        		self.soup=BeautifulSoup(self.data,features="html.parser")
        		print('Conexion establecida.')
        		self.contador=1
        		break
        	except:
        		print('Intento',self.contador,'de conexion fallido.')
        		self.contador=self.contador+1
        		time.sleep(1)
        		if self.contador==6:
        			print('Proceso cerrado despues de 5 intentos.')


    def limpiaHtml(self,link):
        """Función que por parametro admite una variable que será limpiada de código de HTML <>/..."""
        self.resultado=re.sub(r"<.*?>","",str(link))
        return self.resultado


    def escaneoCombinacionGanadora(self):
        """ Este método se usa para obtener los 5 números ganadores desde la web, se obtienen en base a su nombre de clase, se le elimiman caracteres tipicos de HTML,
        y se añade a la lista correspondiente para luego en otro método ser comparada con los numeros jugados por el usuario """
        for link in self.soup.find_all(class_="numeros"):
            self.resultado=self.limpiaHtml(link)
            combinacionGanadora.append(int(self.resultado))


    def estrellas(self): # OJO esta función devuelve una lista y en la función print seleccionamos el index 3
       for link in self.soup.find_all(class_="estrellas"):
            self.resultado=self.limpiaHtml(link)  
            estrellasganadoras.append(int(self.resultado))


    def millon(self):
        for link in self.soup.find_all("span"):
            self.resultado=self.limpiaHtml(link)
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
        print("""Sorteo celebrado el dia:""",fecha[1],
              """\nLos numeros ganadores han sido:""",combinacionGanadora,
              """\nLos numeros jugados han sido:  """,numerosJugados,
              """\nRESULTADOS COINCIDENTES:""",self.numerosComparados,
              """\n""")  
        
        print("""Las estrellas ganadoras han sido:""",estrellasganadoras,
              """\nLas estrellas jugadas han sido:  """,estrellasJugadas,
              """\nRESULTADOS COINCIDENTES:""",self.estrellasComparadas,
              """\n""") 

        print("""El millon ganador ha sido:""",millonganador[3],
              """\nEl millon jugado ha sido: """,millonJugado[0])
        if millonganador[3] == millonJugado[0]:
        	print('¡¡ HAS ACERTADO EL MILLON !!\n\n')
        else:
        	print('NO HAS ACERTADO EL MILLON.\n\n')
       
        print("Has tenido",len(self.numerosComparados),"numeros iguales y",len(self.estrellasComparadas),"estrellas iguales.")
        print("###########################################################################")


    def registrar(self):
        texto=("###########################\nRESULTADO DIA: "+fecha[1]+"\nNumeros ganadores: "+str(combinacionGanadora)+" Numeros jugados:"+str(numerosJugados)+"\nACIERTOS: "+str(self.numerosComparados)+
        "\nEstrellas ganadoras: "+str(estrellasganadoras)+" Estrellas jugadas: "+str(estrellasJugadas)+
        "\nMillon ganador: "+millonganador[3]+" Millon jugado: "+millonJugado[0]+"\n##################\n")   
        registro=open("/volume1/Software/Mis aplicaciones/PYTHON Script Euromillones/resultados.txt","a") # Ruta por defecto del NAS: /volume1/Software/Mis aplicaciones/PYTHON Script Euromillones/resultados.txt
        registro.write(texto)
        registro.close()
        
    
    def __del__(self): # Destructor de clase
        print('Limpiando memoria temporal...')

    

euromillon=web("https://www.euromillones.com.es/")
if euromillon.contador==1: # Accedemos a variable de clase para comprobar su estado
	euromillon.escaneoCombinacionGanadora() # Iniciamos demás operaciones
	euromillon.estrellas()
	euromillon.millon()
	euromillon.fechaSorteo()
	euromillon.calculos()
	euromillon.comprobar_premio()
	euromillon.registrar()
