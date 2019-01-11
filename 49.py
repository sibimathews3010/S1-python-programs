
Conversation opened. 1 read message.

Skip to content
Using Amal Jyothi College of Engineering Mail with screen readers
Enable desktop notifications for Amal Jyothi College of Engineering Mail.
   OK  No thanks
Something's not right.
We're having trouble connecting to Google. We'll keep trying...

3 of 177
(no subject)
Inbox
x

SHAN SHAJI B.Tech CSE B 2018-2022 <shanshaji2022@cs.ajce.in>
Attachments
Tue, Nov 13, 4:45 PM (1 day ago)
to SIDHARTH, me, SHEENA, SIJIN


6 Attachments

d={}
limit=int(input("Enter the number of books: "))
for i in range(limit):
	tit_t=input("Enter the title of the book: ")
	publi_sh=input("Enter the name of the publisher: ")
	no=int(input("Enter the number of copies: "))
	d[(tit_t,publi_sh)]=no
print(d)
print("1.ADD ")
print("2.Remove" )
num=int(input("Enter your option: "))
if num==1:
	title=input("Enter the title of the book: ")
	key=input("Enter the publisher name: ")
	num1=int(input("Enter the number of copies: "))
	d[(title,key)]=d[(title,key)]+num1
	print(d)
elif  num==2:
	title=input("Enter the title of the book: ")
	key=input("Enter the publisher  name: ")
	num1=int(input("Enter the number of copies: "))
	d[(title,key)]=d[(title,key)]-num1
	print(d)
program_49.py
Displaying program_50.py.
