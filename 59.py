a=int(input())
s=str(input())
b=""
c=""
for i in range (len(s)):
	if s[i]=='1':
		b=b+s[i]+" "
	elif s[i]=='0':
		c=c+b
		b=""
print(c.strip())
