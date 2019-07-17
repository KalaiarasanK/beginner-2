A,B=map(int,input().split())
for i in range (1,min(A,B)+1):
	if (A%i==0 and B%i==0):
		X=i
print(X)		
