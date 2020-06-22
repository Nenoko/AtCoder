from sys import stdin
input=stdin.readline

#S=input()
N = int(input())

N-=1

base=ord('a')

print_string=""

while (N >= 26):
  print_string=chr(base+N%26)+print_string
  N //= 26
  N-=1

#print(N)
print_string=chr(base+N%26)+print_string

#print(N)
print(print_string)
#N,K=list(map(int,input().split()))
#P=list(map(int,input().split()))

#P.sort()
#print(sum(P[:K]))

#print(A)