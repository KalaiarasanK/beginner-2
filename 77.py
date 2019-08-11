a=int(input())
b=list(map(int,input().split()))
c=1
d=c
for i in range(len(b)-1):
	if(b[i]<b[i+1]):
		c=c+1
	elif(c>d):
		d=c
		c=1
if(c>d):
	d=c
print(d)
