A=int(input())
Ball=input().split()
B=[]
for i in Ball:
  B.append(i)
B.sort()
B.sort(key=len)
for i in B:
	print(i,end=' ')
