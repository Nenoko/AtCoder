import numpy as np
N,M,C=[int(i)for i in input().split()]
B=np.array([int(b)for b in input().split()])
A=np.array([[int(a)for a in input().split()]for _ in range(N)])
#print([c>0 for c in A*B])
#print([c>0 for c in np.dot(A,B)])
ans=sum([c+C>0 for c in np.dot(A,B)])
#print(B)
#print()
#print(A)
print(ans)