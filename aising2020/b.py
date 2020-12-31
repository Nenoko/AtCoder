N=int(input())
A=list(map(int,input().split()))

print(len([c for c in A[::2]if c%2==1]))