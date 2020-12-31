from collections import defaultdict
def onenum2threenum(num):
  arr=[]
  for i in range(1,num-1):
    for j in range(1, num-i):
        arr.append([i,j,num-i-j])
  return arr

dic=defaultdict(int)

N = int(input())
inp=N
N = (N * 3) ** 0.5 // 1 + 1
N=int(N)

for i in range(3,N+1):
  arr=onenum2threenum(i)
  arr=[(a+b+c)**2-a*b-b*c-c*a for a,b,c in arr]
  for a in arr:
    dic[a]+=1

for i in range(1,inp+1):
  print(dic[i])