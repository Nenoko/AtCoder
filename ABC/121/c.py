import heapq
N, M = [int(i) for i in input().split()]
zaiko={}
value = []
heapq.heapify(value)
for i in range(N):
    #在庫の本数。一本あたりの代金
    b,a=[int(i)for i in input().split()]
    if  b not in zaiko:
        heapq.heappush(value,b)
        zaiko[b]=a
    else:
        zaiko[b]+=a

cnt=0
sumval=0
while True:
    if cnt == M: 
       print(sumval)
       exit()
    minival = heapq.heappop(value)
    minicnt = zaiko[minival]
    #print("minival,minicnt={},{}".format(minival,minicnt))
    if cnt + minicnt <= M:
       cnt+=minicnt
       sumval += minival * minicnt
    else:
       sumval += minival * (M-cnt)
       cnt=M