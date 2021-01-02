N = int(input())
Ss = set()
notSs = set()
for _ in range(N):
    inp = input()
    if inp[0] == "!":
        notSs.add(inp[1:])
    else:
        Ss.add(inp)
#print(Ss)
#print(notSs)
andarea = Ss & notSs
#print(andarea)
if len(andarea) > 0:
    for d in andarea:
        print(d)
        exit()
else:
    print("satisfiable")
# for s in Ss:
#    if s in notSs:
#        print(s)
#        exit()
