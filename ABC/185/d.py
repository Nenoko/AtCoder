import math
N, M = map(int, input().split())
A = list(map(int, input().split()))
if M == 0:
	print(1)
	exit()
if N == M:
	print(0)
	exit()
#area_list=[False]*N
#青スタンプの位置を整列して記録
#for a in A:
#	area_list[a-1]=True
A.sort()
dist = [A[i + 1] - a - 1 for i, a in enumerate(A[:-1])]
if (not A[0] == 1):
	dist.insert(0,A[0]-1)
if (not N==A[-1]):
	dist.append(N-A[-1])
#print(dist)
dist = [d for d in dist if d>0 ]
max_hanko_size = min(dist)

#最適なはんこサイズ=白マスの最小幅
sum_of_loop=0
for w in dist:
	sum_of_loop+=math.ceil(w/max_hanko_size)
print(sum_of_loop)