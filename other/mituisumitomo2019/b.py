import math
N=int(input())
#print(N*100/108)
if N * 100 % 108 == 0:
    print(N*100//108)
else:
    kouho=N * 100 // 108
    for i in range(-1,2):
        #print(math.floor((kouho + i) * 1.08))
        if N == math.floor((kouho + i) * 1.08):
            print(kouho + i)
            exit()
    print(":(")
    