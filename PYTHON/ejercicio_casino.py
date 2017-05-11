# coding:utf-8
from random import randint

saldo=100
salir=False
salir_apuesta=False
apuesta=0
	
if (saldo<10):
	salir_apuesta=True
	salir=True
else:	
	salir_apuesta=False
	print "Saldo actual:" , saldo
	print "Apuesta mínima 10€"
	print "Salir: -1"
	apuesta=input("Introduca su apuesta: ")
			
while (salir_apuesta==False):
	if (apuesta==-1):
		salir_apuesta=True
		salir=True
	else:
		if (apuesta>=10 and apuesta<=saldo):
			saldo=saldo-apuesta
			salir_apuesta=True
		else:
			print "Apuesta incorrecta"
			if (apuesta<10):
				print "La apuesta mínima es de 10€"
			if (apuesta>saldo):
				print "No puede apostar más de su saldo"
				print "Salir: -1"
				apuesta=input("Introduca su apuesta: ")

	
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
		
print "J1", numero , "de", palo1

numero=J2

if (J2==11):
	numero = "J"
		
if (J2==12):
	numero = "Q"
	
if (J2==13):
	numero = "K"

if (J2==14):
	numero = "AS"
		
print "J2", numero , "de", palo2
	

saldo=100
apuesta=0
salir=False



while (salir==False):

	if ("J1"=="J2"):
		print "En caso de empate gana la banca"
		saldo=saldo-apuesta
	else:
		if ("J1"<"J2"):
			print "Usted gana"
			print "J1", numero , "de", palo1
			print "J2", numero , "de", palo2
			saldo=saldo+(apuesta*2)
		else:
			if ("J1">"J2"):
				print "LOOSER!!!"
				saldo=saldo-apuesta
	

			
if (saldo==100):
	print "\nGracias por venir"
else:
	# Ha perdido dinero
	if (saldo<100):
		print "\nCon pardillos como tu me forro"
	else:
		print "\nMe he quedado con tu cara, no vuelvas"
		
	salir=True



