A,B=[int(i) for i in input().split()]
Abin=bin(A)
Bbin = bin(B)
ans=bin(0)
if A - B==0:
    print(Abin)
elif A - B==1:
    print(Abin^Bbin)
else:
    for i in range(len(Bbin)):
        if B % (2 ** i) == 1:
            ans += bin(2 ** i)
    
