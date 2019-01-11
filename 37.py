n=int(input("enter the list size:"))
list=[]
s=0
for i in range(0,n):
	j=int(input( "enter the no:"))
	list=list+[j]
	s=s+list[i]
print("entered list=", list)
print("sum of elements of list=",s)

