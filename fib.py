print("fibnocii series")
l=int(input("enter the last number:"))
n1=0
n2=1
i=0
for i in range(0,l):
	print(n2,end=",")
	nxt=n1+n2
	n1=n2
	n2=nxt
	i=i+1
