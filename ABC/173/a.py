#array=map(int,input().split())
N=int(input())
turi=(N//1000)*1000-N
if turi<0: turi+=1000
print(turi)