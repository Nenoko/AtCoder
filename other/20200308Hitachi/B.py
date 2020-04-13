(_, _, M) = [int(inp) for inp in input().split()]

A = [int(inp) for inp in input().split()]
B = [int(inp) for inp in input().split()]

minA = min(A)
minB = min(B)

min = minA+minB

for m in range(0, M):
    (aindex, bindex, waribiki) = [int(inp) for inp in input().split()]
    newmin = A[aindex-1]+B[bindex-1] -waribiki
    if (newmin < min):
        min=newmin

print(min)