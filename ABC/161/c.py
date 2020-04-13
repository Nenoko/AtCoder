[N,K]=[int(item)for item in input().split()]
while (True):
    tmp = N - K
    if tmp>0:
        N = N%K
        tmp = N - K
    print(abs(tmp) if abs(tmp)<N else N)
    exit()