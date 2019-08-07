a=input()
b=list(map(int,input().split()))
even=evalue=0
odd=ovalue=0
for i in b:
	if(i%2==0):
		even=even+1
		evalue=i
	else:
		odd=odd+1
		ovalue=i
if(even==1):
	print(evalue)
else:
	print(ovalue)
