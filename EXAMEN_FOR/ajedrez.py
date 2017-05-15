
####################################
#  INICAMOS EL BUCLE CON EL FORD   #
####################################

for fil in range(1,9,1):
	for col in range(1,9,1):
		

######################################
#  PRINTAMOS EL TABLERO DE AJEDREZ   #
######################################		
	
		if (fil== 1 or fil==3 or fil== 5 or fil== 7):
		
			if (col %2==0):
				print "B",
		
			else:
				print "N",
				
		else:
			if (col%2==0):
				print "N",
			else:
				print "B",

	print ""
	

