from collections import Counter
N=int(input())
A=[int(item)for item in input().split()]
c=Counter(A)
full = {i: c[i] * (c[i] - 1) / 2 for i in c.keys()}
#full = [full[item-1] for item in A]
#print(full)
#ichiheri = [c[i]-1 * (c[i]-1) / 2 for i in range(1,1+len(c))]
sumA = sum(full.values())
val = {i:int(sumA-full[i]+(c[i]-2) * (c[i]-1) / 2 )for i in c.keys()}
#print(ichiheri)



for a in A:
    print(val[a])