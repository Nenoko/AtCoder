import math
sta,stb=[str(i) for i in input().split()]
a = int(sta)
b = int(stb[0])*100
if stb[1] == '.':
  #小数
  if len(stb) >= 3:
    b+=int(stb[2])*10
  if len(stb) == 4:
    b+=int(stb[3])
print(a*b//100)