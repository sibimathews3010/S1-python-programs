n=int(input("enter the list size:"))
list1=[]

for i in range(0,n):
	j=int(input( "enter the no:"))
	list1=list1+[j]
	
print("entered list1=", list1)

for j in list1:
	if j%2==0:
		list1.remove(j)
print(list1)
