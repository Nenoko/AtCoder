import math
A,B,N = [int(i)for i in input().split()]

def func(A, B, N):
  if N>B-1:
    return math.floor(A*(B-1)/B)-A*math.floor((B-1)/B)
  else:
    return math.floor(A*N/B)-A*math.floor(N/B)


print(func(A,B,N))