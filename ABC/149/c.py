from sys import stdin

input=stdin.readline

def isPrime(x):
  for div in range(2, x // 2 + 1):
    if x % div == 0:
      return False

  return True

X = int(input())

if isPrime(X):
   print(X)
   exit()

while (X < 10 ** 5):
  X+=1
  if isPrime(X):
    print(X)
    exit()

#100000より大きい素数のうち最小のもの
print(100003)