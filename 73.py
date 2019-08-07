a,b=map(int,input().split())
c=list(map(int,input().split()))
d=a-1
for i in c:
	if(c[i]==b):
		d=i
print(d+1)		
