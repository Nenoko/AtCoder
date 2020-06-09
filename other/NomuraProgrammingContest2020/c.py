n = int(input())
A=[int(i)for i in input().split()]
totalcnt = 1
tmpleaf = 2-A[0]
for i in range(1,len(A)-1):
  totalcnt+=tmpleaf
  tmpleaf=(tmpleaf-A[i])*2
  if (i == len(A) - 1) :break
  print(tmpleaf,A[i],totalcnt)

totalcnt+=A[len(A)-1]

print(totalcnt)
  
#3
#0 1 1 2