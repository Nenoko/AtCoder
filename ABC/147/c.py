from collections import defaultdict,deque
N = int(input)
testimony=[]
for n in range(N):
  #未定状態 : -1
  #信頼できる : 1
  #信頼できない : 0
  testimony_of_i=defaultdict(lambda:-1)
  A_i=int(input())
  for a_i in range(A_i):
    x,y=map(int,input().split())
    #"証言"の記録
    testinomy_of_i[x]=y
  testimony.append(testimony_of_i)

  testinomy_of_i=defaultdict(lambda:-1)

  for i,testimony_of_i in enumerate(testimony):
    q = deque([i])
    tmpGraph=testimony_of_i
    #キューが空になるまで全探査を繰り返す
    while len(q) != 0:
      