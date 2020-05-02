N, M, Qnum = [int(i) for i in input().split()]
Q=[[] for _ in range(50)]
for _ in range(Qnum):
  a,b,c,d=[int(i) for i in input().split()]
  Q[a].append([b, c, d])

def searchBestRoute(leftM,a,hitherto_max):
  tmpmax=hitherto_max
  if a == N - 1:
    return hitherto_max
  for a_,samea in enumerate(Q):
    if a_ < a:
      continue
    for q in samea:
      #aとbの差cをコストとみて、ジャンプ(コストの関係で失敗する場合はそもそも飛ばない)
      if leftM-q[1]>=0:
        tmpmax_kouho = searchBestRoute(leftM-q[1],q[0],hitherto_max+q[2])
        tmpmax = tmpmax_kouho if tmpmax_kouho>tmpmax else tmpmax
  return tmpmax

maxval=searchBestRoute(M,0,0)
print(maxval)