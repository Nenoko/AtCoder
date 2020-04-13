import sys
input = sys.stdin.readline

[hukasa, haba] = [int(i) for i in input().split()]

map=[]
for i in range(hukasa):
    numedInp = tuple([True if chr=='#' else False for chr in input()[:-1]])
    map.append(numedInp)
map=tuple(map)

#print(map)

#必ず幅が長くなるようにする
if hukasa > haba:
    map = tuple(zip(*map))
    t = haba
    haba = hukasa
    hukasa=t

#print(map)
#print("{},{}".format(haba,hukasa))

for i in range(0, haba):
    hab = i
    hukas = 0
    for j in range(hukasa):
        print("{},{}".format(hab, hukas))
        hab -= 1
        hukas += 1
        if hab<0 : break

for i in hukasa-1:


