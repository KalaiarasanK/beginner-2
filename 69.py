a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range (b):
	c.pop()
print(end="",*c)
