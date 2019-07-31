a=list(map(int,input().split()))
b=a[len(a)-1]
c=[i for i in input().split()]
for i in c:
	if c.count(str(i))==b:
		print(i)
		break
