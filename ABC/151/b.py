N,K,M=map(int,input().split())
A=list(map(int,input().split()))

sumofA=sum(A)
mokuhyou = M * N - sumofA
print( 0 if mokuhyou<0 else (mokuhyou if mokuhyou<=K else -1))