from collections import Counter
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
#print()
#print(N)
#print(A)
#print(Q)
#print()
counterA = dict(Counter(A))
counterAkeys=set(counterA.keys())
#print(counterAkeys)

sumA = sum(A)

#print(sumA,counterA)
for _ in range(Q):
  b,c=map(int,input().split())
  #print(b,c)
  if b not in counterAkeys:
    print(sumA)
    continue
  b_cnt = counterA[b]
  counterA[b]=0
  if c in counterAkeys:
    counterA[c] += b_cnt
  else:
    counterA[c] = b_cnt
    counterAkeys.add(c)

  sumA+=(c-b)*b_cnt
  print(sumA)