def greatest_three_number(a,b,c):
	if a>b:
		if a>c:
			return a
		else:
			return c
	else:
		if b>c:
			return b
		else:
			return c






a=int(input("enter the number1="))
b=int(input("enter the number2="))
c=int(input("enter the number3="))
G=greatest_three_number(a,b,c)
print("greatest of three no is",G)
