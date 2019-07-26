import sys,string,math,itertools


def minChCnt(S):
	D = {}
	for C in S:
		if not C.isspace():
			D[C] = D.get(C,0) + 1
	min = sys.maxsize
	L = []
	min = min(D.values())
	for K,V in D.items():
		if V == min:
			L.append(K)
	return L

S = input()
N = len(S)
L = minChCnt(S)
print(*L)
