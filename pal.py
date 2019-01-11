print("palentromic series")
N=int(input("enter the number:"))
N1=N
sum1=0
while N>0:
	rem=N%10
	N=N//10
	sum1=sum1*10+rem
if(sum1==N1):
	print(N1,"is palendrome")
else:
	print(N1,"is not palendrome")
	
