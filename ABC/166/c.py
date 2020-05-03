N,M=[int(i)for i in input().split()]
H = [int(i) for i in input().split()]
flag=[True]*N
for _ in range(M):
  A,B=[int(i)for i in input().split()] 
  if H[A-1] <= H[B-1]:
    flag[A-1]=False
  if H[A-1] >= H[B-1]:
    flag[B-1]=False
    
print(flag.count(True))