#! /usr/bin/python
# coding: utf-8

import os, time, stat

path_to_explore="./walk/"
total_size= 0

#MOSTRAMOS EL PESO

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		name_path=os.path.join(root,name)
		print (name_path)
		print os.stat(name_path).st_size
		
		total_size= total_size + os.stat(name_path).st_size
		
	
