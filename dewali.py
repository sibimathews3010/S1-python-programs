print("dewali bonus")
X=int(input("enter the salary X:"))
G=input("enter the gender G:")
S1=X+(X*(2/100))
S2=X+(X*(5/100))
S3=X+(X*(10/100))
S4=X+(X*(2/100))+(X*(10/100))
if(X<10000)and(G=="F"):
	print("salary=",S4)
elif(X<10000)and(G=="M"):
	print("salary=",S1)
elif (X>10000) and (G=="M"):
	print("salary=",S2,"gender=",G)
elif (X>10000)and (G=="F"):
	print("salary=",S3,"gender=",G)

