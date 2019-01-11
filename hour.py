print("sallary for hours")
H=int(input("enter the number of hours worked:"))
Rate=r=int(input("enter the rate:"))
S1=H*10
Rateext=rext=r*1.5
S2=S1+(H-40)*rext
if(H>40):
	print("Salary",S2)
else:
	print("Salary",S1)
