

rang=int(input("enter the number of books to be added"))
dict={}
for i in range(0,rang):
	name=input("enter the name of book :")
	auth=input("enter the name of author :")
	dict[(name,auth)]=int(input("enter the no. of copies :"))
print(dict)
con=input("Do you want to add more of the present book? (y/n)")
if con=="y":
	name=input("enter the name of book :")
	auth=input("enter the name of author :")
	num=int(input("enter the number of copies to be added :"))
	dict[(name,auth)]=(dict[(name,auth)])+num
	
else:
	print("okay...  ;)")
con=input("Do you want to sell the present book? (y/n)")
if con=="y":
	name=input("enter the name of book :")
	auth=input("enter the name of author :")
	num=int(input("enter the number of copies sold :"))
	dict[(name,auth)]=(dict[(name,auth)])-num
	print(dict)
else:
	print("okay...  ;)")

program51.py
Displaying program51.py.
