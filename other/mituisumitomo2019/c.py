import math
X=int(input())
under = math.floor(X / 105)
top = math.floor(X/100)
#print("under,top = {},{}".format(under,top))
if X / 105==under or X/100==top or  top - under > 0:
#if top - under > 0:
    print("1")
else:
    print("0")
#for i in range(under, top + 1):
    