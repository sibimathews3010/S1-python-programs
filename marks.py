print("assessment of marks")
N=input("enter the name :")
print("Name:",N)
m1=int(input("enter subject 1 mark:"))
m2=int(input("enter subject 2 mark:"))
m3=int(input("enter subject 3 mark:"))
m4=int(input("enter subject 4 mark:"))
average=(m1+m2+m3+m4)/4
if m1>=40 and m2>=40 and m3>=40 and m4>=40:
	if average>=75:
		print("distinction")
	elif average>=60:
		print(" first class")
	elif average>=50:
		print("second class")
	else :
		print("third class")
else:
	print("FAIL")
		
