import math
N = [int(i) for i in input()]
Nnum=0
for n in N:
  Nnum*=10
  Nnum += n

buttom=N[0]
top = N[len(N)-1]
keta=math.floor(math.log10(N))+1
cnt=0
for n in (1,99):

  if n < 10:
    if int(str(n) * keta) < N:
      cnt += keta
      if int(str(n)*2)N
    else:
      cnt += keta - 1
  else:

