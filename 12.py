A,B=map(int,input().split())
C=list(map(int,input().split()[:A]))
if B in C:
	print("Yes")
else:
	print("No")
