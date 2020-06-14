X, Y = map(int, input().split())
minAsi = X * 2
maxAsi = X * 4

if Y >= minAsi and Y <= maxAsi and Y % 2 == 0:
  print("Yes")
else:
  print("No")