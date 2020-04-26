from collections import Counter
N=int(input())
array=[]
for i in range(N):
  array.append(input())

c = Counter(array)
print(len(c))