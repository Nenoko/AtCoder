[N, X, Y] = [int(item) for item in input().split()]
X -= 1
Y -= 1
count=[0 for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        count[min(abs(i-j),abs(i-X)+1+abs(Y-j),abs(i-Y)+1+abs(X-j))]+=1
#print(array)


for i in range(1,N):
        print(count[i])

#print(count)