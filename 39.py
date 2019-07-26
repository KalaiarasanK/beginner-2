pow=int(input())
for power in range(100):
	if(pow==2**power):
		print("yes")
		break
else:
	print("no")
