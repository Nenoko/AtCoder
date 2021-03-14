import math
A, B, H = map(int, input().split())
H *= 1000
# みかん数最小->みかん最大
# print(H/B)
minnum = math.ceil(H / B)
maxnum = math.floor(H / A)

if maxnum - minnum < 0:
    print("UNSATISFIABLE")
    exit()

print(minnum, maxnum)
