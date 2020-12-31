import math
#thanks to https://qiita.com/Sirloin/items/333f74a636f194a2310d
# O(k)
#def comb(n,k):
#    nCk = 1
#    MOD = 10**9+7
#
#    for i in range(n-k+1, n+1):
#        nCk *= i
#        nCk %= MOD
#
#    for i in range(1,k+1):
#        nCk *= pow(i,MOD-2,MOD)
#        nCk %= MOD
#    return nCk

L = int(input())
if L == 12:
	print(1)
	exit()
ab = math.factorial(L-1)//(math.factorial(11)*math.factorial(L-1-11))
print(ab)