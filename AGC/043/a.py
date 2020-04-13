import itertools
import sys
input = sys.stdin.readline
[hukasa,haba]=[int(i)for i in input().split()]

map=[]

for i in range(hukasa):
    numedInp = tuple([True if chr=='#' else False for chr in input()])
    map.append(numedInp)
map=tuple(map)

patternTuple=tuple(itertools.combinations(range(hukasa+haba-2),hukasa-1))
#print(len(patternTuple))

print(patternTuple)
min=hukasa+haba-2

for item in patternTuple:
    #print(item)
    flipCnt=0
    renzokuCnt=map[0][0]
    h=0
    w=0
    for i in range(hukasa+haba-2):
        #print("{},{}".format(h,w))
        #白でそれまで黒
        if not map[h][w] and renzokuCnt:
                flipCnt+=1
                if(flipCnt==min):break
                print("{},{}".format(h,w))
        renzokuCnt=map[h][w]
        #itemに数字があるステップは下に行く
        if i in item:
            #下に行く
            h+=1
        else:
            #右に行く
            w+=1
    #最後に連続カウントが溜まっていればフリップ
    if map[h][w]:flipCnt+=1
    if min>flipCnt:
        min=flipCnt
        if min == 0:
            print(min)
            exit()

print(min)