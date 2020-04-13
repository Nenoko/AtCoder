[N,A,B]=[int(item) for item in input().split()]

cnt = N // (A + B) * A
cnt += min(A, N % (A + B))
print(cnt)
