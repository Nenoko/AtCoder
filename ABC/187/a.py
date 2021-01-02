#N=int(input())
#A=list(map(int,input().split()))
A,B=input().split()
asum=0
for a in A:
	a_=int(a)
	asum+=a_
bsum=0
for b in B:
	b_=int(b)
	bsum+=b_
#print(bsum)
print(max(asum,bsum))