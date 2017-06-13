#! /usr/bin/python
# coding: utf-8

import os, stat
path_to_explore="./walk/"	
	
def mi_funcion():	
	for root, dirs, files in os.walk(path_to_explore):
		for name in files:
			name_path= os.path.join(root, name)
			print name_path
			permission= stat.S_IMODE(os.stat(name_path).st_mode)
			permisos= str(oct(permission))
			print permisos
			
permissos= mi_funcion()
print permissos
