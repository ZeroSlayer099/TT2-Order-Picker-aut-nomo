def cambiosector(origen,destino):
	
	p=origen
	f=destino
	#  H I J

	#  F   G
	#  D   E

	#  A B C
	servo='centro'
	
	if(p=='A'):
		if(f=='B' or f=='C' or f=='E'):
			derecho()
		elif(f=='F' or f=='H'):
			cambioS(13)
		elif(f=='I' or f=='J' or f=='G'):
			cambioS(14)
		elif(f=='A' or f=='D'):
			same()
		else:
			salida()
	elif(p=='B'):
		if(f=='C' or f=='E'):
			derecho()
		elif(f=='D'):
			reversa()
		elif(f=='F' or f=='H'):
			cambioS(13)
		elif(f=='I' or f=='J' or f=='G'):
			cambioS(14)
		elif(f=='B'):
			same()
		else:
			salida()
	elif(p=='C'):
		if(f=='D'):
			reversa()
		elif(f=='F' or f=='H'):
			cambioS(23)
		elif(f=='I' or f=='J' or f=='G'):
			cambioS(24)
		elif(f=='C' or f=='E'):
			same()
		else:
			salida()
	elif(p=='D'):
		if(f=='E'):
			derecho()
		elif(f=='F' or f=='H'):
			cambioS(13)
		elif(f=='I' or f=='J' or f=='G'):
			cambioS(14)
		elif(f=='D'):
			same()
		else:
			salida()	
	elif(p=='E'):
		if(f=='F' or f=='H'):
			cambioS(23)
		elif(f=='I' or f=='J' or f=='G'):
			cambioS(24)
		elif(f=='E'):
			same()
		else:
			salida()
	elif(p=='F'):
		if(f=='I' or f=='J' or f=='G'):
			derecho()
		elif(f=='F' or f=='H'):
			same()
		else:
			salida()	
	elif(p=='G'):
		if(f=='I' or f=='H'):
			reversa()
		elif(f=='G' or f=='J'):
			same()
		else:
			salida()	
	elif(p=='H'):
		if(f=='J' or f=='I'):
			derecho()
		elif(f=='H'):
			same()
		else:
			salida()	
	elif(p=='I'):
		if(f=='J'):
			derecho()
		elif(f=='I'):
			same()
		else:
			salida()
	elif(p=='J'):
		if(f=='J'):
			same()
		else:
			salida()		

	print(servo)
sensorin('A','C')
