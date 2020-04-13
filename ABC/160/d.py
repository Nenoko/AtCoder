import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from collections import Counter
[N, X, Y] = [int(item) for item in input().split()]
X -= 1
Y -= 1
gyoretu=np.full((N,N),2000)
gyoretu[0][0]=0
gyoretu[0][1]=1
for i in range(1,N-1):
    gyoretu[i][i-1]=1
    gyoretu[i][i]=0
    gyoretu[i][i+1]=1
gyoretu[N-1][N-2]=1
gyoretu[N-1][N-1]=0

gyoretu[X][Y]=1
gyoretu[Y][X]=1

G=csgraph_from_dense(gyoretu)
#print(G)
d=floyd_warshall(G)
#print(d)
#for k in range(N):
#    for i in range(N):
#        for j in range(N):
#            if gyoretu[i][j]> gyoretu[i][k] + gyoretu[k][j]:
#                gyoretu[i][j] =gyoretu[i][k] + gyoretu[k][j]
#array=[]
#for i in range(N):
#        array += list(d[i][i:])
##c=Counter(array)
#c=Counter(d)
print(d)
d=np.ndarray([np.array(item[i:]).astype('int64')for i,item in enumerate(d)])
print(d)
for i in range(1, N):
    print(np.count_nonzero(d==i))