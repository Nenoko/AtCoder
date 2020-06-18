import sys
input=sys.stdin.readline
N,K=map(int,input().split())
A=list(map(int,input().split()))

contributeSitenaiLamp=[i for i in range(N)]*N

for _ in range(K):
  newA=[0]*N

  for i, a in enumerate(A):
    #contributeしていないものを検索
    for nontributeindex in contributeSitenaiLamp[i]:
      #ランプの明かりが距離より大きければ
      if len(A[nontributeindex]) >= i - nontributeindex:
        contributeSitenaiLamp[i].remove(nontributeindex)
      
    """
    mi=0 if 0>i - a else i-a
    bi=N if N<=i + a+1 else i+a+1
    #print(i,a,mi,bi)
    newA=[j+1 if index>=mi and index<bi else j for index,j in enumerate(newA)]
    """
  A=newA

print(' '.join(map(str, A)))