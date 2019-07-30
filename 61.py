a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=0
for i in range(a-1):
	for j in range(1,a):
		if c[i] + c[j]==b:
			d=1
	if d==0:
		print("no")
		break
else:
	print("yes")
