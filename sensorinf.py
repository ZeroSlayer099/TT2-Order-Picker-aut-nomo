def sensorin(S1,S2,S3,S4,S5,S6,S7,S8):
	s1=S1
	s2=S2
	s3=S3
	s4=S4
	s5=S5
	s6=S6
	s7=S7
	s8=S8
	servo='centro'
	
	if(s1>=800 and s2>=800 and s3>=800)or(s5<800 and s4>=800):
		servo='derecha'
	elif(s6>=800 and s7>=800 and s8>=800)or(s4<800 and s5>=800):
		servo='izquierda'

	print(servo)
sensorin(1000,1000,100,100,100,100,100,100)
