sd=int(input("enter the starting day no"))
l=int(input("enter the length of journey"))
rd=((l%7)+sd)%7
if sd>6:
	print("invalid input")
elif rd==0:
	print("returning day =sunday")
elif rd==1:
	print("returning day =monday")
elif rd==2:
	print("returning day =tuesday")
elif rd==3:
	print("returning day =wedensday")
elif rd==4:
	print("returning day =thursday")
elif rd==5:
	print("returning day =friday")
elif rd==6:
	print("returning day =saturday")

