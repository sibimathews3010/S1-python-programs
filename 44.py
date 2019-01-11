n=int(input("enter the rows in 1st matrix"))
m=int(input("enter the columns in 2nd matrix"))
o=int(input("enter the rows in 2nd matrix"))
p=int(input("enter the columns in 2nd matrix"))
a=[0]*n
for i in range(n):
	a[i]=[0]*m
print("enter the 1st matrix")
for i in range(n):
	for j in range(m):
		a[i][j]=int(input())
b=[0]*o
for i in range(o):
	b[i]=[0]*p
print("enter the 2nd matrix")
for i in range(o):
	for j in range(p):
		b[i][j]=int(input())
c=[0]*n
for i in range(n):
	c[i]=[0]*m
if m==o:
	for i in range(n):
		for j in range(p):
			for k in range(m):
				c[i][j]=c[i][j]+a[i][k]*b[k][j]
print("matrix multiplication")
for i in range(m):
	for j in range(n):
		print(c[i][j],end=" ")
	print()
