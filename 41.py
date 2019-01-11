def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

n=int(input("enter the list size:"))
list1=[]

for i in range(0,n):
	j=str(input( "enter the no:"))
	list1=list1+[j]
	
print("entered list1=", list1)

n=int(input("enter the list size:"))
list2=[]

for p in range(0,n):
	k=str(input( "enter the no:"))
	list2=list2+[k]
	
print("entered list2=", list2)

print(common_data(list1, list2))




