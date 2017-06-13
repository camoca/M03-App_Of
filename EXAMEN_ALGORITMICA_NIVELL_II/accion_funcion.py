#! /usr/bin/python
# coding: utf-8

import os

path_to_explore="./walk/"

def mi_funcion():
	for root, dirs, files in os.walk(path_to_explore):
		for name in files:
			name_path= os.path.join(root, name)
			print name_path
			print os.stat(name_path).st_size
	
peso= mi_funcion()
print peso
