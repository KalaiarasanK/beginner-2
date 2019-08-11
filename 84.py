a=int(input())
b=list(map(int,input().split()))
if len(b)>1:
	C=b[0]|b[1]
else:
	C=b[0]
for i in range(2,a):
	C=C|b[i] 
print((C))
