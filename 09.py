import math
A,B=map(int,input().split()) 
count=0 
for i in range(A,B+1):
	C=math.sqrt(i)
	if(C-math.floor(C)==0):
		count=count+1
print(count)	
