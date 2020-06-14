X, N = map(int, input().split())
P=list(map(int,input().split()))
if not X in P:
  print(X)
  exit()
for i in range(1,100):
  #小さい方向を探す
  if not X - i in P:
    print(X - i)
    exit()
  if not X + i in P:
    print(X + i)
    exit()