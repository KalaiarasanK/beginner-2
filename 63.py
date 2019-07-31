a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b=set(b)
c=set(c)
if(b & c):
	d=sorted(b&c)
	print(*d,end=' ')
