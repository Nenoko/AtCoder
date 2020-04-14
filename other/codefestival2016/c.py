W,H=[int(item) for item in input().split()]
p=[]
for _ in range(W):
    p.append(int(input()))

q=[]
for _ in range(H):
    q.append(int(input()))

#cost = [[114514] * (W+1) for i in range(H+1)]
#cost[0][0]=0
cnt = 1
totalcost=0
while True:
    if cnt <= H :
        x,y=0,cnt
    else:
        x,y=cnt-H,H
        if cnt-H==W+1:break
    while y>=0 and x<=W:
        if x == 0:
            #cost[x][y]=cost[x][y-1]+q[y-1]
            totalcost+=q[y-1]
        elif y == 0:
            #cost[x][y]=cost[x-1][y]+p[x-1]
            totalcost+=p[x-1]
        else:
            totalcost += p[x - 1] if p[x - 1] < q[y - 1] else q[y-1]
            # if cost[x][y - 1] + q[y - 1] < cost[x - 1][y] + p[x - 1]:
            #    cost[x][y]=cost[x][y-1]+q[y-1]
            #    totalcost+=q[y-1]
            # else:
            #    cost[x][y]=cost[x-1][y]+p[x-1]
            #    totalcost += p[x - 1]
        #print(x,y)
        x += 1
        y -= 1
    #print(cnt)
    #print(cost)
    cnt += 1
print(totalcost)