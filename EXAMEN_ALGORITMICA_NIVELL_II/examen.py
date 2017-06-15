#!/usr/bin/python
#coding:utf-8

import os
import stat



def obtener_tamanyo(ruta):
	tamanyo=os.stat(ruta).st_size
	return tamanyo
	
def imprimir_total(cont):
	print "Se han borrado" , cont , "archivos."
	



tamanyo = input("Introduce tamaño maximo: ")
ruta_origen = raw_input("Introduce la ruta del fichero: ")
cont = 0
borrar = os.system('rm -f ')




for ruta, carpetas, arxivos in os.walk(ruta_origen):
    for nombre in arxivos:
		ruta=os.path.join(ruta,nombre)
		tamany=obtener_tamanyo(ruta)
		if (tamany <=tamanyo):
			borrar
			cont = cont + 1
		print ruta , nombre
imprimir_total(cont)
