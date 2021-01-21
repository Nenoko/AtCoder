N=int(input())
S=input()
tmp=0
tmpMax=0
for s in S:
    if s=='I':
        tmp+=1
        if tmpMax<tmp:
            tmpMax=tmp
    else:
        tmp-=1

print(tmpMax)