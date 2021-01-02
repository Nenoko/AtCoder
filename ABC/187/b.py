N=int(input())
cnt=0
X=[]
Y=[]
for _ in range(N):
	x,y=map(int,input().split())
	X.append(x)
	Y.append(y)
for i,(x1,y1) in enumerate(zip(X,Y)):
	for x2,y2 in zip(X[i+1:],Y[i+1:]):
		xdist=abs(x2-x1)
		ydist=abs(y2-y1)
		if xdist==0:
			continue
		katamuki=ydist/xdist
		if katamuki<=1 and katamuki>=0:
			cnt+=1
		#print(katamuki)
print(cnt)
