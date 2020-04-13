[M,N]=[int(item) for item in input().split()]

num={}

for _ in range(N):
    [s,c] = [int(item) for item in input().split()]
    if s > M or  not M==1 and  s == 1 and c == 0:
        print(-1)
        exit()
    if s in num:
        if num[s] == c:
            continue
        else:
            print(-1)
            exit()
    num[s]=c

#print(num)
#数字にする
num_int = 0

if M == 1:
    if  1 in num:
        print(num[1])
    else:
        print(0)
    exit()

if  1 in num:
    num_int = num[1]
else:
    num_int=1

for i in range(2, M + 1):
    num_int*=10
    if i in num:
        num_int+=num[i]

print(num_int)