import math
a,b=map(int,input().split())
c=math.factorial(a)
d=math.factorial(a-b)
e=math.factorial(b)
d=d*e
print(int(c/d))
