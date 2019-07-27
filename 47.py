A,B,C=map(int,input().split(" "))
if(A!=0 and B!=0 and C!=0):
	a=A+B+C
else:
	a=0
if a==180:
	print("yes",end='')
else:
	print("no",end='')
