[K,N]=[int(item) for item in input().split()]
array = [int(item) for item in input().split()]
max_=0
for i in range(N-1):
    dist=abs(array[i] - array[i + 1])
    if dist > max_:
        max_=dist

dist=array[0] + (K-array[N-1])
if dist > max_:
    max_=dist
print(K-max_)