#!/usr/bin/python
#coding:utf-8

import os
import stat



def obtener_permisos(permisos):
	permission=stat.S_IMODE(os.stat(permisos).st_mode)
	permisos=str(oct(permission))
	print permisos
	
def ruta_archivos(ruta):
	ruta=os.path.join(ruta, nombre)

def imprimir_total(cont):
	print "Se han borrado" , cont , "archivos."


permisos= input("Introduce los permisos: ")
ruta_origen= raw_input("Introduce la ruta del fichero: ")
cont = 0
borrar = os.system('rm -f ')




for ruta, carpetas, arxivos in os.walk(ruta_origen):
    for nombre in arxivos:
		permissos=obtener_permisos(ruta)
		if (permissos <= permisos ):
			borrar
			cont = cont + 1
		print ruta , nombre
imprimir_total(cont)
