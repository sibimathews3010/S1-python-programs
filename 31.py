def Fibonaci(n):

	if(n==0):
		return 0

	elif(n==1):
		return 1

	else:
		return Fibonaci(n-1) + Fibonaci(n-2)



n = int(input("Enter the no: "))

for i in range(n):
	print(Fibonaci(i))

