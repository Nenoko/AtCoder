from operator import mul
from functools import reduce

MOD=(10**9+7)

def cmb(n,r):
    r = min(n-r,r)
    ret=1
    for i in range(n - r + 1, r + 1):
        ret *= i
        ret%=MOD

def mod(a):
    modded = a % MOD
    return modded if modded>=0 else modded+MOD
    
[n,a,b]=[int(item)for item in input().split()]
modn=n%MOD
print(mod(mod(mod(2**modn)-mod(cmb(n,a)))-mod(cmb(n,b))-1))
#print(cmb(modn,a))