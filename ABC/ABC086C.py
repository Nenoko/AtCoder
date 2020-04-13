N=int(input())
txy = []

for _ in range(N):
   tmptxy=[int(row )for row in input().split()]
   txy.append(tmptxy)

t = 0
x = 0
y = 0
for i in range(N):
    tdist=txy[i][0]-t
    xdist = abs(x - txy[i][1])
    ydist = abs(y - txy[i][2])
    #print("tdist,xdist,ydist={},{},{}".format(tdist,xdist,ydist))
    if xdist+ydist-tdist<=0 and (xdist + ydist-tdist) % 2 == 0:
        t = txy[i][0]
        x = txy[i][1]
        y = txy[i][2]
        continue
    else:
        print("No")
        exit()

print("Yes")