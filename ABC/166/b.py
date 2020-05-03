from collections import Counter
N,K=[int(i)for i in input().split()]
c=Counter([])
for i in range(K):
  input()
  c+=Counter([int(i)for i in input().split()])
  
#print(len(c.keys()))
print(N-len(c.keys()))