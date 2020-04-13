N = int(input())
mochi=[]
for _ in range(N):
    inp = input()
    if not inp in mochi:
        mochi.append(inp)

print(len(mochi))