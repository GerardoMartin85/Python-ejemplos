""" Docstring del string, fichero que automatiza descarga del fichero geoip desde su web, descomprime dicho fichero elimina la última versión instalada y copia el fichero a su localización"""
# coding: utf-8
import shutil
import urllib.request
import locale
import datetime
from os import remove
import sys
import os
# Versión del 20/05/2020 ##############################################################################################################



# Variables ##########################################################################################################################
dt = datetime.datetime.now()																		# Variable que captura fecha y hora de la descarga y del proceso
fechahora=""																						# Variable vacía que conforme pasa el código va cogiendo
tamano=""
captura_fechahorainicio=""

# Funciones generales ##############################################################################################################
def fecha_hora():
	"""Función que cada vez que se le llama captura la fecha y hora en el formato elegido y lo devuelve en variable fechahora"""
	dt = datetime.datetime.now()
	fechahora="{}:{}:{} - {}/{}/{}".format(dt.hour,dt.minute,dt.second,dt.day,dt.month,dt.year) 
	return fechahora

def escribe_error(error):																			
	"""Guarda aviso de error en fichero txt, admite un parámetro que será una cadena como por ejemplo Error 1, Error 2..."""
	captura_fechahora=fecha_hora()																	# Ejecuta la función fecha_hora y guarda valor en variable.
	log1=open("/volume1/web/logs/log_script_python.txt","a", encoding="utf-8")						# Abre y sitúa puntero al final del documento de texto.
	log1.write("ACTUALIZACIÓN FALLIDA: Inicio:{}, Finalización:{}, Error:{}.\n".format(captura_fechahorainicio,captura_fechahora,error)) # Escribe en documento de texto lo indicado.
	log1.close(); captura_fechahora=""																# Cierra documento de texto y borra variable.

""" Códigos de error creados:
Error 0: indica que no se ha podido conectar al servidor de descarga
Error 1: indica que el fallo está en la descomprensión del fichero o en la eliminación del fichero descargado
Error 2: indica que el fallo está a la hora de verificar el nombre fichero descomprimido.
"""

def escribe_ok():
	"""Guarda aviso de correcto en fichero txt"""
	captura_fechahora=fecha_hora()
	log1=open("/volume1/web/logs/log_script_python.txt","a", encoding="utf-8")
	log1.write("ACTUALIZACIÓN CORRECTA: Inicio:{}, Finalizada:{}, tamaño:{} Bytes.\n".format(captura_fechahorainicio,captura_fechahora,tamano)) 
	log1.close(); captura_fechahora=""		



# Script ##############################################################################################################
captura_fechahorainicio=fecha_hora()																# Captura la fecha y hora del inicio del proceso
print("HORA DE COMIENZO:",captura_fechahorainicio)
try:
	print("Comenzando descarga...")
	url = 'http://chir.ag/projects/geoiploc/autogen/geoiploc.tar.gz' 								# Variable con dirección del fichero a bajar
	archivo_tmp, header = urllib.request.urlretrieve(url) 											# Obtención del fichero comprimido y pasa a variable
	dt = datetime.datetime.now() 																	# Variable que captura fecha y hora de la descarga y del proceso
	captura_fechahora=fecha_hora() 
	tamano=os.path.getsize("geoiploc.php") 															# Obtiene el tamaño del fichero indicado y devuelve un entero
except:
	escribe_error("0, no se ha podido conectar al servidor de descarga.")							# Error 0, indica que el fallo está a la hora de la conexión y descarga del fichero.
	
try:
	with open('/volume1/web/logs/info.tar.gz', 'wb') as archivo:
		with open(archivo_tmp, 'rb') as tmp:
			archivo.write(tmp.read())
	ficherotar=shutil.unpack_archive('/volume1/web/logs/info.tar.gz',"/volume1/web/logs/") 			# primera posición significa ruta y nombre de fichero donde almacenarlo
	remove("/volume1/web/logs/info.tar.gz") 														# Eliminación del fichero
	if os.path.isfile("geoiploc.php")==True: 														# Verifica que el fichero indicado existe en esa carpeta devuelve True o False
		print("Espacio ocupado: {} Bytes, actualizacion correcta: {}\n".format(tamano,fechahora)) 	# Muestra confirmación por consola, en el synology no admite salida por consola con utf-8 asi que no admite acentos, ñ...
		log=open("/volume1/web/logs/geoiploc.txt","w", encoding="utf-8") 							# encoding soluciona problemas a la hora de pasar acentos, Ñ...
		log.write("{}".format(fechahora)) 															# Abre fichero y añade fecha y hora de la variable anterior
		log.close()
		escribe_ok()
		print("HORA DE FINALIZACIÓN:",fecha_hora())
	else:
		print("Se ha producido algún error en el proceso de captura del fichero desde:",url,"volver a intentar actualización manualmente...")
		escribe_error(error="2, descarga ok, pero error a la hora de la descompresión.")			# Error 2 indica que el fallo está a la hora de verificar el nombre fichero
except:
	print("Error en el proceso de captura del fichero desde:",url,"volver a intentar actualización manualmente...")
	escribe_error(error="1, archivo comprimido no encontrado, PROCESO FINALIZADO, REINTENTAR SCRIPT DE NUEVO.")	# Error 1 indica que el fallo está en la descomprensión del fichero o en la eliminación del descargado
	


