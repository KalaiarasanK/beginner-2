a,b=map(str,input().split())
a=list(a)
b=int(b)
c=-1
for i in range(0,b+1):
	if(str(i) in a):
		c=c+1
if(c==b):
	print("yes")
else:
	print("no")
