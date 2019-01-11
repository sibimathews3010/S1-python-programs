n = int(input("ENTER THE NO. OF TERMS "))

a =[]
c = 0
for i in range(0,n):
	j=int(input("ENTER THE NO. "))
	a=a+[j]

s = int(input("ENTER THE ITEM TO BE COUNTED "))

for i in range(0,n):
	if a[i] == s:
		c = c+1	
b = tuple(a)


print(b)
print("THE NO. OF TIMES",s,"APPEARS IS ",c)
