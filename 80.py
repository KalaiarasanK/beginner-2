a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(len(b)):
	for j in range(i+1,len(b)):
		t=abs(b[i]-b[j])
		if t==0:
			continue
		c.append(t)
print(min(c)) 
