s=list(input().split())
a=s[0]
b=s[1]
for i in a:
	if(i in b):
		print("yes")
		exit()
print("no")
