a=int(input())
b=list(map(int,input().split()))
b.append(-1) 
c=[]
for i in range (a-1):
	c.append(max(b[i],b[i+1]))
if a==1:
	print(b[0])
else:
	for i in range(len(c)-1):
		print(c[i],end=' ')
	print(c[len(c)-1])
