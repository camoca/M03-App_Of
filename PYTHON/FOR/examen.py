for fil in range(1,9,1):
	for col in range(1,9,1):
		if ((fil %2 ==0) or (col %2==0)):
			print "*",
			
		if ((fil %2 ==1) or (col %2==1)):
			print "*"
		
		else:	
			print ""
			
	print " "
