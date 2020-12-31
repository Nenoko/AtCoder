N=int(input())
L=list(map(int,input().split()))

L.sort()

cnt=0
for i, a in enumerate(L):
  if i==len(L)-2:break
  for j, b in enumerate(L[i+1:]):
    j = i+j+1
    if j==len(L)-1:break
    cnt+=len([c for c in L[j+1:]if c < a + b])
print(cnt)