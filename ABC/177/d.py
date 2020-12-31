M,N = map(int, input().split())
sets=[set() for m in range(0,M+1)]
for _ in range(N):
  a,b = map(int, input().split())
  sets[a].add(b)
  sets[b].add(a)

print(sets)
#グラフの作成
newsets=[]
for set_ in sets[1:]:
  
max=0
print(max)