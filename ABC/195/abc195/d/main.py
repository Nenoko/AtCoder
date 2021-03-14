import math
import numpy as np
#S = input()
#N = int(input())
#S = input().split()
#A, B, C = input().split()
#L = list(map(int, input().split()))
N, M, Q = map(int, input().split())

WV = []
for _ in range(N):
    WV.append(tuple(map(int, input().split())))

WV.sort(key=lambda x: -1*x[1])
# print(WV)

X = list(map(int, input().split()))

placeable = []
for x in X:
    placeable_ = []
    for (w, v) in WV:
        if x >= w:
            placeable_.append(v)
    placeable.append(placeable_)

# print(placeable)
for _ in range(Q):
    # greedy?
    L, R = map(int, input().split())
    # 0オリジン化
    L -= 1
    R -= 1
    newX = X[:L] + X[R + 1:]
    new_placeable = placeable[:L] + placeable[R + 1:]
    new_placeable_sorted_index = np.argsort(np.array(newX))
    new_placeable = np.array(new_placeable)[new_placeable_sorted_index]

    new_placeable = new_placeable[-1::-1]
    #print(newX, new_placeable_sorted_index, new_placeable)
    tmpvalue = 0

#    print(new_placeable)
    for w, v in WV:
        for i, box in enumerate(new_placeable):
            #            print(w, v, i, box)
            if v in box:
                # 箱を占拠する
                tmpvalue += v
                new_placeable = np.delete(new_placeable, i, axis=0)
                break
           # print(v, new_placeable)
#    print(tmpvalue)
    #print(L, R, new_placeable)
