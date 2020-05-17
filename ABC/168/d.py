[N,M]=[int(i)for i in input().split()]
#setの配列を持つ
edge=[set() for _ in range(N+1)]
#print(edge,shortestPath)
for i in range(M):
  [a,b]=[int(i)for i in input().split()]
  #print(a,b)
  edge[a].add(b)
  edge[b].add(a)
#print(edge)

shortestPath=[N+1]*(N+1)
shortestPath[1]=0
nextEdgeKouho=set([1])
#1番目の部屋から最短距離を更新して行く
while(len(nextEdgeKouho)>0):
  nextNextEdgeKouho = set([])
  for start in nextEdgeKouho:
    tmpshortestpath=shortestPath[start]
    for end in edge[start]:
      if shortestPath[end] == N+1:
        shortestPath[end] = start
        nextNextEdgeKouho.add(end)
  #print(nextNextEdgeKouho)
  nextEdgeKouho=nextNextEdgeKouho
#print()
#print(shortestPath[2:])
if N + 1 in shortestPath[1:]:
  print("No")
else:
  print("Yes")
  [print(i) for i in shortestPath[2:]]