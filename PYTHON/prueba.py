#coding: utf8


from random import randint

saldo=100
apuesta=0
salir_apuesta= False
salir= False

while (salir==False):
	
	print "tienes", saldo, "€"
	apuesta= input('Elija una opcion, apuesta o se retira: ')
	
	
	if ( apuesta == -1) or (saldo > 10): 
		salir= True
	
	else:
		if (apuesta > saldo):
			print "No puedes apostar tanto dinero"
		else:
			if (apuesta < 10):
				print "Minimo se apuestan 10€"
			else:
				
				while (salir_apuesta == False):

					palo=randint(1,4)

					if (palo==1):
						palo1 = "Picas"
	
					if (palo==2):
						palo1 = "Rombos"
	
					if (palo==3):
						palo1 = "Trebol"
	
					if (palo==4):
						palo1 = "Corazones"
	

					palo=randint(1,4)
							
					if (palo==1):
						palos2 = "Picas"
						
					if (palo==2):
						palos2 = "Rombos"
							
					if (palo==3):
						palos2 = "Trebol"
							
					if (palo==4):
						palos2 = "Corazones"
	

					J1=randint(2,14)
					J2=randint(2,14)

					numero1=J1
					
					if (J1==11):
						numero1 = "J"
							
					if (J1==12):
						numero1 = "Q"
							
					if (J1==13):
						numero1 = "K"

					if (J1==14):
						numero1 = "AS"
							
					print "Tienes un", numero1 , "de", palo1
					
					numero2=J2
					
					if (J2==11):
						numero2 = "J"
							
					if (J2==12):
						numero2 = "Q"
						
					if (J2==13):
						numero2 = "K"

					if (J2==14):
						numero2 = "AS"
						
					print "Tu rival tiene un", numero2 , "de", palos2
						
					if (J1 == J2):
						print "Gana la banca" 
						saldo= saldo - apuesta
					else:
						if (J1 > J2):
							print "YOU WIN"
							saldo = saldo + apuesta 
						else:
							if (J1 < J2):
								print "YOU LOSE"
								saldo= saldo - apuesta
