num=int(input())
list=[]
for i in range (1,num+1):
	if num%i==0:
		list.append(i)
for num in list:
	if num%2!=0:
		print(num,end=" ")
