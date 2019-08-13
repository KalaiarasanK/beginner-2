import math
a,b=map(int,input().split())
c=math.factorial(a)
d=math.factorial(a-b)
print(int(c/d))
