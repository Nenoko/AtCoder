import itertools
N,K=map(int,input().split())

weight_array=[]
for _ in range(N):
    tmparray=list(map(int,input().split()))
    weight_array.append(tmparray)
#print(weight_array)
    
seq=[i for i in range(1,N)]
pattern=list(itertools.permutations(seq))
#print(pattern)
cnt=0
for l in pattern:
    tmpcost=0
    pred = 0
    for nex in l:
      tmpcost += weight_array[pred][nex]
      pred=nex
    #都市1に戻ってくる
    tmpcost+=weight_array[pred][0]
    if tmpcost == K:
        cnt+=1
    #print(tmpcost)
print(cnt)
    