numero= 1
total= 0

for numero in xrange (1,6):
	if (numero %2 ==0):
		print numero
		total= total + numero
		
	if (numero== 5):
		print total
