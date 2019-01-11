n=int(input("enter the no.of rows in 1st matrix"))
m=int(input("enter the no.of columns in 1st matrix"))
a=[0]*n
for i in range(n):
	a[i]=[0]*m
print("enter the 1st matrix")
for i in range(n):
	for j in range(m):
		a[i][j]=int(input())
b=[0]*n
for i in range(n):
	b[i]=[0]*m
print("enter the 2nd matrix")
for i in range(n):
	for j in range(m):
		b[i][j]=int(input())
c=[0]*n
for i in range(n):
	c[i]=[0]*m

d=[0]*n
for i in range(n):
	d[i]=[0]*m

		
		

print("added matrix")
for i in range(m):
	for j in range(n):
		c[i][j]=a[i][j]+b[i][j]
		print(c[i][j],end=" ")
print("subtracted matrix")
for i in range(m):
	for j in range(n):
		d[i][j]=a[i][j]-b[i][j]
		print(d[i][j],end=" ")
