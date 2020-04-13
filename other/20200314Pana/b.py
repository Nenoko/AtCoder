[H,W]=[int(inp) for inp in input().split()]
if H == 1 or W == 1:
    print(1)
    exit()
yokoKisu = H // 2 + H % 2

sum=H*(W//2)+yokoKisu*(W%2)
print(sum)