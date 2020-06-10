from sys import stdin

input=stdin.readline

#ユークリッド互除法
def gcd(a, b):
  dekai = max(a, b)
  tiisai = min(a, b)
  
  div = dekai % tiisai
  next_dived=tiisai
  #次割られるのは，さっき割り込んできたやつ
  #次割るのは，さっきの計算で出た余り
  while (div != 0):
    tmp=div
    div = next_dived % div
    next_dived=tmp

  return next_dived

A,B=map(int,input().split())

#print(gcd(A,B))

print (A*B//gcd(A,B))