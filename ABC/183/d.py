N,W=map(int,input().split())
S=[]
T=[]
P=[]
timeline=[]

for _ in range(N):
  s,t,p=map(int,input().split())
  S.append(s)
  T.append(t)
  P.append(p)
maxt=max(T)
maxpool=[0 for _ in range(maxt)]
for s,t,p in zip(S,T,P):
    for i in range(s, t):
        maxpool[i]+=p
        if maxpool[i] > W:
            print('No')
            exit()

print('Yes')


