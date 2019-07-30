a=int(input())
if a%2!=0:
	print("1")
else:
	B=True
	for i in range(2,a):
		if a%i==0 and int(a/i)%2!=0:
			b=False
			print(i)
			break
	if b:
		print(a)
