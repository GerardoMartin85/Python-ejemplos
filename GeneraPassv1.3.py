""" Aplicación que genera contraseñas seguras de distintos tamaños y tipos, desarrollada por Gerardo Martín, Mayo 2020 """
# -*- coding: utf-8 -*-										# Codificación utf, ¡ESENCIAL INDICAR ESTO!
import random 											# Para generar números aleatorios
import os 											# Para funciones del sistema, por ahora solo borrar o vaciar consola
from string import punctuation, ascii_letters, digits 						# Cadenas de caracteres, números y símbolos
import datetime 										# Para Fecha y hora
import time 											# Funciones de tiempo para el sistema, en este caso se usara para la variable que cierra la aplicación una vez pasados X segundos.

# VARIABLES #########################################################################################################################################
datos=("1.3",15,"Python Versión 3.8.2")		            					# Tupla en variable con datos que se necesitarán por orden de posición (versión, tiempo en segundos para cierre)
pass_opcion1 = ascii_letters+digits+punctuation 						# Variable que contiene todos los carácteres ASCI disponibles, desde números, letras y símbolos en una cadena.
# Contenido de la variable anterior: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
pass_opcion2 = ascii_letters+digits 								# Variable que contiene todos los carácteres, números y letras en una cadena.
pass_opcion3 = ascii_letters 									# Variable que contiene todos las letras en una cadena.
datetime=datetime.datetime.now() 								# Variable donde almacenaremos la hora.
secure_random = random.SystemRandom()								# Variable que donde se llama al método SystemRandom y se genera de forma segura la contraseña.
password=None											# Inicialización de variable password como None
info={"Autor":"Gerardo Martín","Fecha":"Mayo 2020","S.O.":"Windows 7, 8, 8.1 y 10","email":"geramv22@hotmail.com"}	# Diccionario con varios datos de la aplicación.
base_datos="bd1,6million.txt" 												# Están disponibles:bd1,6million.txt y bd29Million.txt ésta última al ser excesivamente grande da fallos en ciertos equipos.


# FUNCIONES #########################################################################################################################################
def graba_pass(nombrefichero,password):
	"""DOCSTRING DE la Función que efectúa grabación de la contraseña
	generada en un fichero con nombre personalizado,
	ambos datos entran por parámetros. """
	try:
		archivo=open("{}.txt".format(nombrefichero),"w",encoding="utf8")
		archivo.write(password)
		archivo.close()
	except:											# Captura de posibles errores que pudieran producirse a la hora de la grabación del fichero.
		print("Error a la hora de guardar el fichero con la contraseña, revise que tiene permisos de lectura/escritura en la carpeta donde está trabajando, vuelva a intentarlo mas tarde.")

# CODIGO ###########################################################################################################################################
print("Bienvenido a la aplicación GeneraPass versión",datos[0]) 			# Versión de la aplicación, procede de variable datos es una tupla, obtenemos posición 0
print("") # Expacio en blanco
print("""Escriba una de las 4 opciones disponibles:
1. Contraseña muy segura (incluye números, caracteres especiales y letras mayúsculas/minúsculas).
2. Contraseña segura (incluye letras mayúsculas/minúsculas y números)
3. Contraseña normal (sólo letras  mayúsculas/minúsculas)
4. Contraseña tipo palabra de X tamaño (NO RECOMENDABLE).""")


while True:
	try:										# Try, intentar realizar las operaciones de abajo y si fallan te mete en el except
		entrada = int(input("Escriba el número de opción: ")) # Input para meter por consola datos el usuario a esta variable la cual será convertida en entera si es posible, si no actua el except.
		if entrada>=0 and entrada<=4: # El flujo de programación de entrada empieza en este if si el valor es mayor o igual que 0 y menor o igual que 4, rompe proceso y bluce finaliza ok
			break
		else:
			print("Por favor escriba una opción del 1 al 5.") # Si el flujo de programación no ha entrado en el if, entra en este Else y comienza el bucle.
	except:	# Captura todos los errores que se podrían producir entre el Try y el except y en caso de que haya algún error muestra el print en pantalla y el programa continua
		print("Error, has introducido un caracter erróneo,solo admite números.")

while True:
	try:
		tamano=int(input("Escriba el tamaño de contraseña que desea (máximo 16.000.000 caracteres):"))
		if tamano>=0 and tamano<=16000000:
			print("")
			break
	except:
		print("Error, has introducido un caracter erróneo,solo admite números.")

print("")											# Impresión de espacio en blanco
os.system("clear") 										# Para Unix/Linux/MacOS/BSD, vacía la línea de comandos
os.system("cls")										# Para Windows, vacía la línea de comandos
print("Has seleccionado la opción número",entrada,"y de tamaño",tamano,"caracteres.")
nombrefichero=str(input("Introduzca un nombre para el fichero donde se almacenará la clave (pulsar intro para un nombre automático):"))
if nombrefichero=="": 										# Si nombrefichero es cadena vacía, nos mete en if para genera un nombre conforme a la hora y fecha de ese instante
	nombrefichero=str("{}_{}_{}-{}{}{}".format(datetime.hour,datetime.minute,datetime.second,datetime.day,datetime.month,datetime.year)) # Generamos variable con los datos de fecha y hora en el momento de la lectura

if entrada==1:											# En caso de que la variable entrada sea 1 nos mete en este if.
  print("Se está generando la clave...")
  password="".join(secure_random.choice(pass_opcion1) for i in range(tamano)) # Proceso de generación de la contraseña aleatoria usando la unión de loscaracteres que el for en rango
  graba_pass(nombrefichero,password)								# de la variable tamano nos genera X carácteres y los almacena en password para posteriormente meter los argumentos en la función

elif entrada==2:										# En caso de que la variable entrada sea 2 nos mete en este if.
  print("Se está generando la clave...")
  password="".join(secure_random.choice(pass_opcion2) for i in range(tamano))
  graba_pass(nombrefichero,password)

elif entrada==3:										# En caso de que la variable entrada sea 3 nos mete en este if.
	print("Se está generando la clave...")
	password="".join(secure_random.choice(pass_opcion3) for i in range(tamano))
	graba_pass(nombrefichero,password)

elif entrada==4:
	try:
		bd=open(base_datos,"r")
		lineas=bd.readlines()
		print("Procesando... puede tardar un poco, la base de datos contiene",len(lineas),"posibilidades.") # Contamos números de registros en el fichero.
		bd.close()
		random.shuffle(lineas)								# Desordena la lista líneas aleatoriamente
		for x in lineas:
			if len(x)-1==tamano:			# If para cribar las palabras que sean de igual tamaño que la variable introducida en tamaño, se elimina uno porque todos las líneas tienen un intro al final.
				password=x							# Nos pasa a variable el primer valor encontrado X con igual tamaño que "tamano"
		graba_pass(nombrefichero,password)						# Efectúa la creación del fichero .txt
	except:
		print("\nError, fichero de base de datos no enontrado, proceso abortado.")

														

print("")											# Impresión de espacio en blanco
#os.system("clear") 										# Para Unix/Linux/MacOS/BSD, vacía la línea de comandos
#os.system("cls") 										# Para DOS/Windows, vacía la línea de comandos
print("Tu contraseña es:",password) 								# Mostrando contraseña por consola.
print("Se ha generado un fichero llamado {}.txt junto a esta aplicación, muchas gracias por usar este software.".format(nombrefichero))
print("Sistemas operativos compatibles:",info["S.O."],"\nAutor:",info["Autor"],"\nemail:",info["email"],"\nFecha:",info["Fecha"],"\nDesarrollado bajo:",datos[2],) # Llamada a diccionario info y tupla datos
print("")
print("EN {} SEGUNDOS SE CERRARÁ LA APLICACIÓN.".format(datos[1]))			# Variable datos es una tupla, obtenemos posición 1
time.sleep(datos[1]) 										# Cerrar aplicación en 15 segundos, procede de variable datos es una tupla, obtenemos posición 1
