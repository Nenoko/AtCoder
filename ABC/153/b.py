H,N=[int(i)for i in input().split()]
A=[int(i)for i in input().split()]
print("Yes" if sum(sorted(A)[:N])>=H else "No")
