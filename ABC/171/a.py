from sys import stdin
input=stdin.readline

S=input()
aord=ord('a')

if ord(S[0]) < aord:
  print('A')
else:
  print('a')
#A=list(map(int,input().split()))
#print(A)