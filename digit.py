print("sum of digits of a number")
N=int(input("enter the number:"))
sum=0
while N>0:
	rem=N%10
	N=N//10
	sum=rem+sum
print("SUM=",sum)
