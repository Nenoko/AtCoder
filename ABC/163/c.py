from collections import Counter
N =int(input())
A = [int(i) for i in input().split()]

c = Counter(A)
for i in range(1,N+1):
    print(c[i])