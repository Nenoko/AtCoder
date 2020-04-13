import sys
input=sys.stdin.readline
S=input().splitlines()[0]
Q = int(input())
flipcnt=0
for _ in range(Q):
    q = input().split()
    if len(q) == 1:
        flipcnt += 1
        continue
    else:
        if (int(q[1]) + flipcnt) % 2 == 1:
            #前
            S=q[2]+S
        else:
            S=S+q[2]
    #print(S)

if flipcnt % 2 == 1:
    S=S[::-1]

print(S)