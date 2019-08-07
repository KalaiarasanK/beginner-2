a=input()
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
	for j in range(i+1,len(b)):
		if(b[i]<b[j]):
			c=c+1
print(c)			
