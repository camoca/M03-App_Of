#coding: utf8

from random import randint

	saldo=100
	apuesta=0
	salir=True
	salir_apuesta= False
	apuesta= raw_input('Elija una opcion, apuesta o se retira: ')

apuesta()
jugada()

def apuesta():

	saldo=100
	apuesta=0
	salir=True
	salir_apuesta= False
	apuesta= raw_input('Elija una opcion, apuesta o se retira: ')

	while (salir_apuesta == False):

		if ( apuesta == -1) or (apuesta > 10): 
			salir= True	
			salir_apuesta= True
		else:
			if (apuesta >= 10 and saldo< 10) :
				salir_apuesta= True
			
				

apuesta()		
		
def jugada():	
	
	saldo=100
	apuesta=0
	salir=True
	salir_apuesta= False
	apuesta= raw_input('Elija una opcion, apuesta o se retira: ')

	salir= False
	while (salir==False):

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
		palo2 = "Picas"
		
	if (palo==2):
		palo2 = "Rombos"
		
	if (palo==3):
		palo2 = "Trebol"
		
	if (palo==4):
		palo2 = "Corazones"
		

	J1=randint(2,14)
	J2=randint(2,14)

	numero=J1
	
	if (J1==11):
		numero = "J"
			
	if (J1==12):
		numero = "Q"
			
	if (J1==13):
		numero = "K"

	if (J1==14):
		numero = "AS"
			
	print "Tienes un", numero , "de", palo1
	
	numero=J2
	
	if (J2==11):
		numero = "J"
			
	if (J2==12):
		numero = "Q"
		
	if (J2==13):
		numero = "K"

	if (J2==14):
		numero = "AS"
		
		if (J1 == J2):
			print "Gana la banca"
			saldo = saldo - apuesta 
		else:
			if (J1 > J2):
				print "YOU WIN"
				saldo = saldo + apuesta *2
			else:
				if (J1 < J2):
					print "YOU LOSE"
					saldo = saldo - apuesta
	if (saldo < 10):
		salir= True

	while (salir_apuesta == False):

		if ( apuesta == -1) or (apuesta > 10): 
			salir= True	
			salir_apuesta= True
		else:
			if (apuesta >= 10 and saldo< 10) :
				salir_apuesta= True
			
apuesta()
jugada()
