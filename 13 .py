A=int(input())
B=[]
for i in range(0,A):
	B.append(list(map(int,input().split())))
C=0
D=0
for i in range(0,A):
	for j in range(0,A):
		if B[i][j]==1:
			if i!=A-1 and B[i+1][j]==0:
				C=C+1
			if j!=A-1 and B[i][j+1]==0:
				C=C+1
			if i!=0 and B[i-1][j]==0:
				C=C+1
			if  j!=0 and B[i][j-1]==0:
				C=C+1
			if i==0 and j==0 or i==A-1 and j==A-1 or i==0 and j==A-1 or i==A-1 and j==0 and C==2:
				D=D+1
			elif i==1 and j>0 and j<A-1 and C==3:
					D=D+1
			elif C==4:
				D=D+1
		C=0	
print(D)		
