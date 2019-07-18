A,B=map(int,input().split())
input()
C=list(map(int,input().split()))
H=list(map(int,input().split()))
for i in H:
	C.append(i)
	print(max(C),end=' ')	
