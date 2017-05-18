palo=["1","2","3","4"]
numeros=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
cont= 52
from random import randint

for palo in range(1,5,1):
	for numeros in range(1,14,1):
		palo=randint(1,4)
		numeros=randint(1,13)
		if(numeros == 11):
			numeros= "J"
			
		if(numeros == 12):
			numeros= "Q"
			
		if(numeros == 13):
			numeros= "K"
			
		if(palo == 1):
			palo= "D"
			
		if(palo == 2):
			palo= "C"
			
		if(palo == 3):
			palo= "T"
		
		if(palo == 4):
			palo= "P"
				
		print numeros, palo
		
	cont= cont- 1
	


