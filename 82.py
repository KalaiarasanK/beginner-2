a=int(input())
b=list(map(int,input().split()))
if len(b)>1:
	c=b[0]&b[1]
else:
	c=b[0]
for i in range(2,a):
	c=c&b[i] 
print((c))
