num=int(input())
for i in range(2,num):
	if num%i==0:
		print("yes")
		break
else:
	print("no")
