Num=int(input())
a=input().split(" ")
list=[]
if(len(a)==Num):
	for i in sorted (a):
		list.append(i)
if(list==a):
	print("yes")
else:
	print("no")
