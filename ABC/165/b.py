import math
X=int(input())
start=math.ceil(math.log(X/100,1.01))
kouza=100
for i in range(0,1000000):
  kouza=math.floor(kouza*1.01)
  #if i % 100 == 0:
    #print(kouza)
  if kouza >= X:
    print(i+1)
    break