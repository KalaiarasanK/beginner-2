p,a=map(int,input().split())
x=[(k,l) for k in range (p) for l in range (p) if k+l==(p/2) and k*l==a] 
if len(x)>0:
	print("yes",end="")
else:
	print("no",end="")
