N,K=[int(i)for i in input().split()]
H = [int(i) for i in input().split()]
print(sum(sorted(H)[::-1][K:]))
#print(sum(sorted(H)[K::-1]))