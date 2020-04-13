[a,b,c]=[int(inp) for inp in input().split()]
#if a*a+b*b+c*c -2*(a*b+b*c+c*a) > 0:
if c - a - b < 0 or a*(a-2*b)+b*(b-2*c)+c*(c-2*a)<=0:
    print("No")
else:
    print("Yes")