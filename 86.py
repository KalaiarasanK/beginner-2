a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
	for j in range(i+1,a):
		c=b[i]^b[j]
print(c)		
