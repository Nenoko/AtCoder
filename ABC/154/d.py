[N,K]=[int(item)for item in input().split()]
p = [int(item) for item in input().split()]
su = sum(p[0:K])
maxsu=su
ind=0
for i in range(0, N-K):
    su=su - p[i] + p[i + K ]
    if su > maxsu:
        ind = i+1
        maxsu=su
#print("{},{}".format(su,maxsu))
#print(p[ind:ind+K])
#print([n*(n+1)/(2*n) for n in p[ind:ind+K]])
print(sum([n*(n+1)/(2*n) for n in p[ind:ind+K]]))