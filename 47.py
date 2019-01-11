n = int(input("ENTER THE NO. OF TERMS "))
s = 0
a =[]

for i in range(0,n):
	j=int(input("ENTER THE NO. "))
	a=a+[j]

for i in range(0,n):
	if i == n-1:
		break
	if a[i] < a[i+1]:
		t = a[i]
		a[i]=a[i+1]
		a[i+1]=t
print("LARGEST NO. IS ",a[n-2]) 
b = tuple(a)			


for i in range(0,n):
	if i == n-1:
		break
	if a[i] > a[i+1]:
		t = a[i]
		a[i]=a[i+1]
		a[i+1]=t
print("SMALLEST NO. IS ",a[n-2]) 
			



