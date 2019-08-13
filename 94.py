a=str(input())
b=0
for i in range(0,len(a)):
	for j in range(i+1,len(a)):
		if(a[i]==a[j]):
			b+=1
if(b>=1):
	print("yes")
else:
	print("no")
