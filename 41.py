N,M=map(int,input().split())
gate=1
for i in range(1,100):
	if(pow(M,i)==N):
		print("yes")
		gate=0
		break
if(gate==1):
	print("no")
