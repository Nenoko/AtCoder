[N,M]=[int(item)for item in input().split()]
items=[int(item)for item in input().split()]
items_sum=sum(items)

cnt=0
for item in items:
    if item >= items_sum /(4*M):
        cnt += 1
        if cnt==M:
            print("Yes")
            exit()
        
print("No")