for n in range(100,200+1):
	f=0
	for i in range (1,n+1):
	
		if (n%i==0):
			f=f+1
	if(f==2):
		print(n,end="\n")
	#prime numbers in the range 100 to 200
