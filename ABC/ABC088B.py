N=input()
a=[int(inp) for inp in  input().split()]
#print("N,a=[{},{}]".format(N,a))

sortedA=sorted(a)
alice=0

#print("sortedarray=[{}]".format(sortedA))

for i, val in enumerate(sortedA[::-1]):
    alice+= int(val) if i%2==0 else -int(val)     

print(alice)