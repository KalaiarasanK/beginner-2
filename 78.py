a,b=map(int,input().split()) 
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in d:
	c.append(i)
c.sort()
print(*c,end=" ")
