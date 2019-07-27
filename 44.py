num,kalai=input().split()
kalai=int(kalai)
for i in range (kalai):
	num=num[-1] + num[:-1]
print(num,end=' ')	
