from sys import stdin
input=stdin.readline

#S=input()
N,K=list(map(int,input().split()))
P=list(map(int,input().split()))

P.sort()
print(sum(P[:K]))

#print(A)