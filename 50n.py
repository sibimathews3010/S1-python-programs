

num=int(input("enter the  number of items to be added to the dictionary: "))
dict={}
for i in range(num):
	n=input("enter the key")
	dict[n]=input("enter the value")
	num=num+1
print(dict)
c=input("WHICH IS THE KEY TO BE DELETED??")
del dict[c]
c=input("NEXT DELETION TO??")
del dict[c]
print("AFTER DLETION")
print(dict)

program50.py
Displaying program50.py.
