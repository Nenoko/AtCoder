N, K = map(int, input().split())

strN = str(N)

for _ in range(K):
    min_strN = ''.join(sorted(strN))
    max_strN = ''.join(sorted(strN)[::-1])
    #print(min_strN,max_strN)
    strN = str(int(max_strN) - int(min_strN))
print(strN)