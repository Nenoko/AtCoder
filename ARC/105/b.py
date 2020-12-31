import math

N=int(input())
A = list(set(map(int, input().split())))
a=A[0]
gcd = a
for a in A[1:]:
    gcd = math.gcd(gcd,a)

print(gcd)




"""
heapq.heapify(a)
min_a = heapq.heappop(a)
a=list(map(lambda x: x*(-1), a))

while True:
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        print(max_a)
        break
    else:
        a.remove(max_a)
        a.add(max_a-min_a)

while True:
    max_a=heapq.heappop(a) * -1
    if max_a == min_a:
        print(min_a)
        break
    next_added = max_a - min_a
    if next_added < min_a:
        min_a = next_added
    if next_added*-1 not in a:
        heapq.heappush(a,next_added*-1)
"""