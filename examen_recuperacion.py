#! /usr/bin/python
# coding: utf-8
cont=0
tamany= input("Introduzca el tamaño: ")
carpeta= input("Introduzca la carpeta: ")

import os, stat
import commands
os.system('rm -rf')
comando= os.system('rm -rf')

path_to_explore="./walk/"

def mi_funcion():
	for root, dirs, files in os.walk(path_to_explore):
		for name in files:
			name_path= os.path.join(root, name)
			print name_path
			print os.stat(name_path).st_size
			
			if(name_path < tamany):
				comando
	for root, dirs, files in os.walk(path_to_explore):
		for name in dirs:
			print name
			
peso= mi_funcion()
print peso
