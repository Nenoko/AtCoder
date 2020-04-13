N=int(input())
A=[int(item) for item in input().split()]
S=set()
for i in range(N):
    if A[i] in S:
        print("NO")
        exit()
    else:
        S.add(A[i])

print("YES")
