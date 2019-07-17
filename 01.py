A,B=list(map(int,input().split()))
C,D=list(map(int,input().split()))
E,F=list(map(int,input().split()))
if A==B or C==D or E==F or A==C==E or B==D==F:
	print("yes")
else:
	print("no")
