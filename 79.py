a=int(input())
b=list(map(int,input().split()))[:a]
c=[]
for i in range(0,a):
	for j in range(1,a):
		d=abs(b[i]-b[j])
		c.append(d)
print(max(c)) 
