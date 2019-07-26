S1=int(input())
count=0
for i in range(S1):
	s1,s2=map(int,input().split())
	if s1<s2:
		count+=1
print(count,end='')		
