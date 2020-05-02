import math
K=int(input())
A,B=[int(i)for i in input().split()]
a=math.ceil(A/K)
print("OK" if B>=a*K else "NG")
