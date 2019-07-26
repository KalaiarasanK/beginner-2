even=int(input())
list=[]
for i in range(2,even+1):
	if(even%i==0):
		list.append(i)
for num in list:
	if(num%2==0):
		print(num,end=" ")
