n=int(input("enter the list size:"))
list=[]

for i in range(0,n):
	j=str(input( "enter the no:"))
	list=list+[j]
	
print("entered list=", list)
for j in list :

	if len(j)>=2:
	
		if (j[0])==(j[-1]):
			print (j)



