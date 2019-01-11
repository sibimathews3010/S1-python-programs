

centr={"Double Side":0.75,"single side":1,"Black and White":1, "Colour ":5, "Sprial Binding":25}
doub=int(input("enter the number of pages in Double Side :"))
sing=int(input("enter the number of pages in Single side :"))
bw=int(input("enter the number of pages in black and white :"))
clr=int(input("enter the number of pages in colour :"))
spb=int(input("enter the number of pages in Spiral Binding :"))
centr["Double Side"]=centr["Double Side"]*doub
centr["single side"]=centr["single side"]*sing
centr["Black and White"]=centr["Black and White"]*bw
centr["Colour"]=centr["Colour"]*clr
centr["Double Side"]=centr["Double Side"]*spb


