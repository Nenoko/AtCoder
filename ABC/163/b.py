N, M = [int(i) for i in input().split()]
A=[int(i) for i in input().split()]
sumA=sum(A)
print(N-sumA if N-sumA>-1 else -1)
