N,M,K=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

cnt=0

#Aのみ読んだ場合を考える
for a in A:
  if K >= a:
    K-=a
    cnt+=1
  else:
    break

maxcnt=cnt
A=A[: cnt ]
#print(A,K)
for i,b in enumerate(B):
  #aの要素なくしてbを入れる
  #bがいれれるまでaをなくすよ
  while b>K and len(A)!=0:
    a = A.pop()
    K += a
    cnt -= 1
    #print('-a,',a,K)
    
  if len(A) == 0:
    _B=B.copy()[i:]
   # print(_B)
    _B.pop(0)
    #まだbが入るかもしれない…！
    while(K>=b):
      K-=b
      cnt+=1
      #print('+b(while),',b,K,cnt)
      if len(_B) == 0:
        break
      b=_B.pop(0)
    if maxcnt < cnt:
      maxcnt=cnt
    break

  K -= b
  cnt+=1
  #print('+b,',b,K,cnt)
  
  if maxcnt < cnt:
    maxcnt=cnt



print(maxcnt)    