n=int(input("enter the list size:"))
list=[]
for i in range(0,n):
	j=int(input( "enter the no:"))
	list=list+[j]
	
print("entered list=", list)
k=list[0]
for large in list:
	if large>k:
		k=large
print(k)


