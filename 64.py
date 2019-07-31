a=[int(i) for i in input().split()]
n=a[0]
k=a[1]
a=[int(i) for i in input().split()]
a.sort()
r=[]
for i in a:
	if(i<k):
		r.append(i)
print(end="",*r)
