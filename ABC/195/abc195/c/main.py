import math
# S = input()
N = int(input())
# S = input().split()
# A, B, C = input().split()
# L = list(map(int, input().split()))
# H, N = map(int, input().split())

if N <= 999:
    print(0)
    exit()

cnt = 0

for i in range(1, 15):
    # 一個上で見る
    if N >= 10 ** (3*i):
        cnt += N-(10**(3*i)-1)
    else:
        print(cnt)
        exit()
