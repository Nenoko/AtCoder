
K=int(input())
S=input()
printwords=S[:K]
if len(S) > K:
  printwords+="..."
print(printwords)
