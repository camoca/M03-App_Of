from random import randint 
salir= False
salir2= False

while (salir== False):
	
	J1palo= randint(1,4)
	J2palo= randint(1,4)
	
	if (J1palo == 1):
		palo1= "Picas"
		
	if (J1palo == 1):
		palo1= "Diamantes"
	
	if (J1palo == 1):
		palo1= "Treboles"
	
	if (J1palo == 1):
		palo1= "Corazones"
		
	J1= randint(2,14)
	J2= randint(2,14)
	
	numero1= J1
	
	if(J1== 11):
		numero1= "J" 
		
	if(J1== 12):
		numero1= "Q" 
		
	if(J1== 13):
		numero1= "K" 
		
	if(J1== 14):
		numero1= "AS" 
		
	print "Tienes un", numero1, "de", palo1
	
	while(salir2== False):
		
		if ((J1==J2)and(J1palo== J2palo)):
			J2= randint(2,14)
			J2palo= randint(1,4)
			
		if not ((J1==J2)and(J1palo== J2palo)):
			salir2= True
			
	if(J2palo== 1):
		palo2= "Picas"
		
	if(J2palo== 2):
		palo2= "Diamantes"
		
	if(J2palo== 3):
		palo2= "Treboles"
		
	if(J2palo== 4):
		palo2= "Corazones"
		
	numero2= J2
	
	if (J2== 11):
		numero2= "J"
		
	if (J2== 12):
		numero2= "Q"
		
	if (J2== 13):
		numero2= "K"
		
	if (J2== 14):
		numero2= "AS"
		
	print "El rival tiene", numero2, "de", palo2
	
	if (J1== J2):
		print "EMPATE"
		
	else:
			if(J1> J2):
				print "HAS GANADO"
			else:
				print"HAS PERDIDO"
				
	if not(J1> J2):
		salir=True
