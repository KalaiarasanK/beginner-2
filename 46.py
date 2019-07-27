import math
a=int(input())
b=math.radians(a)
c=math.sin(b)
if b<1:
	print(round(c,1))
else:
	print(round(c)) 
