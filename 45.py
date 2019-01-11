n = int(input("ENTER THE NO. OF TERMS "))

a =[]

for i in range(0,n):
	j=int(input("ENTER THE NO. "))
	a=a+[j]

s = int(input("ENTER THE ITEM TO BE DELETED "))

for i in range(0,n):
	if a[i] == s:
		a.remove(s)	
b = tuple(a)


print(b)

