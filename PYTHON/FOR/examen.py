for fil in range(1,5,1):
	for col in range(1,4,1):
		if (fil==1):
			if (col==2):
				print "A"
			if (col==3):
				print "B"
			if (col==4):
				print "C"
				
			else:
				print "---"
		if(col==1):
			print fil-1
		
		if(fil==3 and col==3):
			print "*"
		
		if(fil==4 and col==2):
			print "*"
