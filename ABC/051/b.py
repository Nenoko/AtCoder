K,S=map(int,input().split())

cnt=0
for x in range(K + 1)[::-1]:
  S_=S-x  
  #S_をyzで分割する．条件を壊さないよう注意
  z_saitei = S_ - K if S_ <= 2*K else 0
  z_saidai = K if  S_ > K else S_
  
  if z_saidai - z_saitei >= 0:
    print(x,z_saitei,z_saidai)
    cnt += z_saidai - z_saitei + 1

print(cnt)