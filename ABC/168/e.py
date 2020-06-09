N=int(input())
A=[]
B=[]
#N*Nのコスト
cost = [[[]for _ in range(N)] for i in range(N)]
for i in range(N):
  a,b=[int(i)for i in input().split()]
  A.append(a)
  B.append(b)

