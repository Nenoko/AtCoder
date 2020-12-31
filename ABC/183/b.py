sx,sy,gx,gy=map(int,input().split())
#print(sx, sy, gx, gy)

#gyを逆転させる

gy*=-1

#y=ax+b
a = (gy - sy) / (gx - sx)
b=sy-a*sx

tekisetuna_x=-1*b/a
print(tekisetuna_x)