import math
[A,B,H,M]=[int(i)for i in input().split()]
#print(A, B, H, M)
totalhun=H*60+M
zisinkakudo=totalhun/720*360
hunsinkakudo = M * 6
#print(hunsinkakudo,zisinkakudo)
aidanokakudo=min(zisinkakudo-hunsinkakudo,360-(zisinkakudo-hunsinkakudo))
c=(A**2+B**2-2*A*B*math.cos(math.radians(aidanokakudo)))**(0.5)
print(c)