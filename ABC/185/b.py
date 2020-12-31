N, M, T = map(int, input().split())
A=[]
B = []
tmpTime=0
first_N=N
for _ in range(M):
	a,b=map(int,input().split())
	#A.append(a)
	#B.append(b)
	#減少
	N-=(a-tmpTime)
	if N <= 0:
		print("No")
		exit()
	#上昇
	N += (b - a)
	if (N > first_N):
		N=first_N
	tmpTime=b
N-=T-tmpTime
#print(N)
if N > 0:
	print("Yes")
else:
	print("No")


