import math
N=int(input())
A=list(map(int,input().split()))

#整数にする
y=round(sum(A)/N)
#print(y)
hituyou_min_cost=sum([(x-y)**2 for x in A])
print(hituyou_min_cost)