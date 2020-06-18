import math
from collections import Counter
import sys

input=sys.stdin.readline

N = int(input())
A=list(map(int,input().split()))

#O(nlogn)
A.sort()

if len(A) == 0:
  print(0)
  exit()


cnt= 0 if len(A)>1 and A[0]!=A[1] else -1

while len(A)>0:
  #iの先頭要素を取り出す
  a = A[0]
  #aで割り切れるやつは削除する
  A = [a_ for a_ in A if a_ % a != 0]
  cnt += 1
  
print(cnt)