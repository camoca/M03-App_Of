import os
path_to_explore="/.walk"
def mostrar_directorios(	for root, dirs, files in os.walk (path_to_explore):
		for name in files:
			print name
print "" ):

print mostrar_directorios
