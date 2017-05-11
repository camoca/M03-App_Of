for fil in range(1,5,1):
	for col in range(1,9,1):
		if(fil==1):
			print "*",
		
		elif(fil==4):
			print "*",
			
		elif(col==1):
			print "*",
			
		elif(col==8):
			print"*",
			
		elif(((col==4) or (col==5)) and (fil==2)):
			print ".",
			
		elif((col==4) and (fil==3)):
			print "\\",	
			
		elif((col==5) and (fil==3)):
			print "/",

		else:		
			print "",

	print" " 
