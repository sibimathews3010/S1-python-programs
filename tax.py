print("chargable tax")
S=int(input("enter the income="))
T1=0
T2=S*(10/100)
T3=S*(20/100)
T4=S*(30/100)
if(S<150000):
	print("tax=",T1)
elif (150000<=S<=300000):
	print("tax=",T2)
elif (300000<S<=500000):
	print("tax=",T3)
elif (S>500000):
	print("tax=",T4)
