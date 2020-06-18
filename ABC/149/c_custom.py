from sys import stdin
import math

input=stdin.readline

def isPrime(x):
  if x % 2 == 0:
    return False
  for div in range(3, math.floor(x **(0.5)) + 1,2):
    if x % div == 0:
      return False

  return True

X = int(input())
if X == 2:
  print(2)
  exit()

if X % 2 == 0:
  X+=1

if isPrime(X):
   print(X)
   exit()

while (True):
  X += 2
  if isPrime(X):
    print(X)
    exit()
