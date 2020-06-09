tenzyou=10**18
input()
A=[int(i) for i in input().split()]
if 0 in A:
  print(0)
  exit()
sortedA=sorted(A)[::-1]
multi = 1
for a in A:
  multi *= a
  if multi > tenzyou:
    print(-1)
    exit()

print(multi)
