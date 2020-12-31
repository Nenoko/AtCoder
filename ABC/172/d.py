import math
N = int(input())
yakusuulist = [-1] * N
yakusuulist[1]==1
sum_=0
for n in range(1,N):
  for div in range(2,math.ceil(n ** (0.5))):
    if n % div == 0:
      dived = n // div

  sum_+=n*(yakusuulist[div]+yakusuulist[dived])