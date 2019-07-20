A,B,C=map(str,input().split())
C=int(C)
D=len(A)
E=0
for i in range(D):
	if(A[i]!=B[i]):
		E=E+1 
if(E==C):
	print("yes")
else:
	print("no") 
