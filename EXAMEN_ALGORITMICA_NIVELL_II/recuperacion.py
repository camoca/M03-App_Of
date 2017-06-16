import os, stat, time

path_to_explore='./walk'

def imprimir_todo1(cont1):
	print "El numero total de directorios es: ", cont1
	
def imprimir_todo2(cont2):
	print "El numero total de ficheros es: ", cont2
	
cont1= 0
cont2= 0

for root, dirs, files in os.walk(path_to_explore):
	for name in dirs:
		name_path= os.path.join(root,name)
		print name_path
		cont1= cont1 + 1
		
	for name in files:
		name_path=os.path.join(root, name)
		print name_path
		print "El fichero ocupa: ", os.stat(name_path).st_size
		print"la ultima fecha de modificacion es: ", time.ctime(os.path.getmtime(name_path))
		cont2= cont2 + 1
			
imprimir_todo1(cont1)
imprimir_todo2(cont2)	
