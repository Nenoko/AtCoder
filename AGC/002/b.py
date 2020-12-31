from collections import defaultdict

N, M = map(int, input().split())

ball_count=[1 for _ in range(N)]
redExist=[0 for _ in range(N)]
redExist[0]=1
for m in range(M):
  x, y = map(int, input().split())
  #1オリジンから0オリジンに
  x-=1
  y-=1

  ball_count[x] -= 1
  ball_count[y] += 1
  if (redExist[x]):
    redExist[y]=True
  if ball_count[x] == 0:
    redExist[x]=False
print(len([b for b in redExist if b]))
