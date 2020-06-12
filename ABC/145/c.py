N = int(input())
X = []
Y = []
sum=0
#距離の和を計算
for _ in range(N):
  x,y=map(int,input().split())
  for i, [x_,y_] in enumerate(zip(X,Y)):
    sum+=((x-x_)**2+(y-y_)**2)**(0.5)
  X.append(x)
  Y.append(y)

print(sum*2/N)