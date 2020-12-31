def flipXandTransDecimalnum(X, keta):
  #print(X)
  X=[c if not keta==i else ('1' if c=='0' else '0' )for i,c in enumerate(X) ]
  #print(X)
  X.reverse()
  su=0
  for i in range(0,len(X)):
    su+=int(X[i])*2**i
  return su
def popcount(X):
  cnt=0
  while (X > 0):
    cnt+=X%2
    X//=2
  return cnt
N=int(input())
X=input()

"""
for i in range(100):
  print(popcount(i))

"""
for i in range(len(X)):
  intX=flipXandTransDecimalnum(X,i)
  for j in range(intX):
    pop=popcount(intX)
    #print(intX,pop)
    intX = intX % pop
    if intX == 0:
      print(j+1)
      break