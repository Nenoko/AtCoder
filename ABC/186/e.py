	
T = int(input())
N = []
S = []
K = []
for _ in range(T):
	n,s,k=map(int,input().split())
	N.append(n)
	S.append(s)
	K.append(k)
for n,s,k in zip(N,S,K):
	i_ = 0
	while True:
		if s == k:
			print(i_-1)
			break
		i=(n-s)//k
		nextS=(i+1)*k+s-n
		if nextS == s%k:
			print(-1)
			break
		s = nextS
		i_ += i + 1
