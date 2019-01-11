print("largest of three numbers")
X=int(input("enter first no="))
Y=int(input("enter second no="))
Z=int(input("enter third no="))
if(X>Y):
	if(X>Z):
		print("X largest;",X)
	else:
		print("Z larget;",Z)
else:
	print("Y largest",Y)

