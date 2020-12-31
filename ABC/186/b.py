import math
H, W = map(int, input().split())
mat = []
sum_=0
for h in range(H):
	row=map(int,input().split())
	mat.extend(row)
	#sum_+=sum(row)
min_num = min(mat)
#print(mean)
#print(mat)

print(sum([abs(min_num-m) for m in mat]))