import sys
input = sys.stdin.readline
k=int(input().split()[1])
source = [int(i) for i in input().split()]

target = []
nagasa=len(source)

for j in range(nagasa):
    num=source[j]
    for i in range(j+1, nagasa):
        target.append(num*source[i])
#target=[source[y]*source[x]for y in range(nagasa) for x in range(y+1,nagasa)]
target.sort()
#print(sorted_target[k-1])
print(target[k-1])