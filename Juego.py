"""Juego desarrollado por Gerardo Martín para realizar ejercicio del curso de Aula 10, el juego consiste en una aplicación
que genera un número aleatorio en un rango definido por usuario y dependiendo de si está en modo automático (IA) o normal (jugador)
vamos buscando nosotros ese número hasta ganar o perder si gastamos todas las vidas que también nos genera la aplicación en base al
rango previamente definido, en modo automático la CPU automaticamente va generando número dentro de ese rango y comprobando si son
el que previamente ha generado ella o no también pudiendo ganar o pudiendo perder"""

import random # Importación modulo de random para generar números aleatorios en determinadas situaciones
import sys # Importación modulo de sistema para ejecutar cierre de sistema pero finalmente no se implementa
from modulos.J_f_m import Entrada # Importación desde carpeta modulos fichero J_f_m función Entrada
from modulos.final import fin # Importación desde carpeta modulos fichero final función fin
from time import time # Importación modulo time para calcular el tiempo de las jugadas

suerte=0
print("Bienvenido al juego de adivinar números, desarrollado en Python por Gerardo Martín")
print("Seleccione una opción para jugar:")
print("1. Jugador normal")
print("2. CPU (Juego automático con Inteligencia artíficial)")
seleccion=input("Seleccione una opción: ")
seleccion=int(seleccion)
if seleccion==1:
    print("....Modo jugador activado....") # Terminamos el if para que ejecute el módulo ya situado en línea 43
elif seleccion==2:
    juego1=Entrada() # Funcion del modulo J_f_m.py
    print("....Jugando la IA de tu equipo....")
    numero1=random.randint(0,juego1) # Generamos un número aleatorio entre el 0 y el de la variable juego
    vidas=round(juego1/10000+10) # Generamos un número de vidas diviendo juego1 entre tal y sumando 10 para tener como mínimo siempre 10
    intentos1=vidas # Creamos variable intentos1 con el número de vidas
    def randomly(seq):
    	shuffled=list(seq)
    	random.shuffle(shuffled)
    	return iter(shuffled)
    print("Dispongo de",vidas,"intentos, ¡COMENZAMOS!");hora1=time()
    for n in randomly(range(juego1)): # Modulo for para iterar en el rango aleatorio de var juego1
        print("He seleccionado el número",n,".");hora2=time()
        if n==numero1:
            print("")
            hora2=time();hora3=hora2-hora1
            print("¡He ganado el número secreto es el",n,"!","HE TARDADO",round(hora3,2),"segundos.")
            final1=input(" ")
            break
        else:
            vidas-=1
            hora2=time();hora3=hora2-hora1
            print("¡Y he fallado, me quedan",vidas,"intentos!","HE TARDADO",round(hora3,2),"segundos.")
            print("")
            if vidas==0:
                print("¡No he sido capaz de encontrar el número en",intentos1,"intentos y he perdido, el número era el",numero1,"!")
                final1=input(" ")
                break

juego=Entrada() # Funcion del modulo J_f_m.py            
numero = random.randint(0, juego) # Creación del número aleatorio, entre 0 y variable juego introducida por usuario
vidas=round(juego/100+3) # Vidas, se redondea calculando la variable juego introducida por el usuario diviendo entre 100 y sumando 4
suerte=int(suerte) # Creación de variable suerte para almacenar el número que escribirá el usuario para probar suerte

print("¡Suerte, tienes",vidas,"intentos!")
print("") # Espacio en blanco
def Jugando(suerte):
    """Se mete el número que quiere probar el usuario en suerte, se verifica que este número sea 
    mayor, menor o igual que la variable numero (generada automaticamente entre la variable juego 
    (indicada por usuario) y el 0) se añade la puerta trasera 28102018 para ganar automaticamente"""
    global vidas
    while True:
        suerte=input("¡Juega!: ")
        print("")
        try:
            suerte=int(suerte)
            if suerte==numero:
                print("¡Ganaste, el número",suerte,"era el número secreto...!")
                final=input("...¡Enhorabuena!... ")
                break

            elif suerte==28102017: # modo trampa por si no adivinamos el número así ganar seguro.
                print("¡TRAMPOSO! el número secreto es el {}.".format(numero))
                final=input("...... ")
                break

            elif suerte>numero:
                print("Inténtalo de nuevo el número secreto es mas pequeño!")
                vidas-=1
                print("Te quedan",vidas,"intentos")
                print("")
                if vidas==0:
                    print("¡¡HAS PERDIDO!!, el número era el {}.".format(numero))
                    fin() # Funcion fin del modulo final.py
                    print("¡¡HAS PERDIDO!!, el número era el {}.".format(numero))
                    final1=input(" ")
                    break
                    
            elif suerte<numero:
                print("Inténtalo de nuevo el número secreto es mas grande!")
                vidas-=1
                print("Te quedan",vidas,"intentos")
                print("")
                if vidas==0:
                    print("¡¡HAS PERDIDO!!, el número era el {}.".format(numero))
                    fin() # Funcion fin del modulo final.py
                    print("¡¡HAS PERDIDO!!, el número era el {}.".format(numero))
                    final1=input(" ")
                    break
                             
        except:
            print("¡Solamente puedes indicar números!") # En caso de que no entre por try muestra el except
            vidas-=1
            print("¡Te quedan",vidas,"intentos, ya que te estoy quitando por equivocarte también!")

Inicio=Jugando(suerte) # Inicio del juego
