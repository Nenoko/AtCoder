N=int(input())
P = [int(i) for i in input().split()]
min = P[0]
lowelemcnt=1
for p in P[1:]:
  if min >= p:
    lowelemcnt += 1
    min=p
print(lowelemcnt)
    