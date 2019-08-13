a=int(input())
b=list(map(int,input().split()))
for i in range(0,a-1,2):
	b[i],b[i+1]=b[i+1],b[i]
print(*b)	
