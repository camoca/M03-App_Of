#! /usr/bin/python
# coding: utf-8

import os

path_to_explore="./walk/"

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
		print (name_path)
	
