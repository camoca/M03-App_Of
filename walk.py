#! /usr/bin/python
# coding: utf-8

import os
import stat

path_to_explore="./walk/"

total_size= 0

#MOSTREM NOMES ELS DIRECTORIS

for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:
		print name
		
print "------------------------------------------------"

#MOSTREM NOMES ELS ARXIUS

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		print name
		
print "------------------------------------------------"

#MOSTREM TOT

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		print name
		
	for name in dirs:
		print name
		
print "------------------------------------------------"

#MOSTREM RUTAS DELS ARXIUS

for root, dirs, files  in os.walk(path_to_explore):
	for name in files:
		
		name_path=os.path.join(root, name)
		print (name_path)
	
print "------------------------------------------------"

#MOSTREM RUTA DELS DIRECTORIS

for root, dirs, files  in os.walk(path_to_explore):
	for name in dirs:
		
		name_path=os.path.join(root, name)
		print (name_path),
		
#MOATREM EL PES
	
		print os.stat(name_path).st_size
		
		total_size= total_size + os.stat(name_path).st_size
		
#MOSTREM ELS PERMISOS
		
		permission= stat.S_IMODE (os.stat(name_path).st_mode)
		permisos= str(oct(permission))
		print permisos
		
		other= permisos[3:4]
		if(other=="0"):
			print "todo bien todo correcto"
		else:
			print "CAUTION"
