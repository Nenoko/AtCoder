N,M=map(int,input().split())
W=list(map(int,input().split()))
L=[]
V=[]
for _ in range(M):
  l,v=map(int,input().split())
  L.append(l)
  V.append(v)

if max(W) > max(V):
    print(-1)
    exit()

dist = [[0] * N for i in range(N)]
for i,w1 in enumerate(W):
    for j,w2 in enumerate(W[i+1:]):
        #print(w1+w2,i,i+j+1)
        weight_sum = w1 + w2
        for k, v in enumerate(V):
            print(v,weight_sum,L[k])
            if v < weight_sum:
                #最低保証
                #上三角行列として使うことにする
                print()
                for d in dist:
                    print(d)
                dist[i][i + j+1] = L[k]
                for d in dist:
                    print(d)
                print()

for d in dist:
    print(d)
