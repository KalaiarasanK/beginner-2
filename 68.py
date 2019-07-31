a=int(input())
b=list(map(int,input().split()))
c=1
d=c
r=1
for i in range(a-1):
	if(b[i]==b[i+1]):
		c=c+1
		r=c
	elif(c>d):
		d=c
		r=c
		c=1
print(r)
