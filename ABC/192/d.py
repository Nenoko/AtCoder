X = input()
M = int(input())
Xaslist = [int(x) for x in X]

Xaslist_reversed=Xaslist[::-1]
#最大桁数がわかる
mind = max(Xaslist)+1

def multiplyAsDigit(d):
    sum_of_x = Xaslist_reversed[0]
    tmpd=d
    for x in Xaslist_reversed[1:]:
        sum_of_x += x * tmpd
        tmpd *= d
    
    return sum_of_x

#print(multiplyAsDigit(4))
#mindの時点で可能性が満たされる場合がる
result=multiplyAsDigit(mind)
if result > M:
    #満たせるdがない
    print(0)
    exit()
elif len(X) == 1:
    print(1)
    exit()
#上限を求める
searching_mind=mind
maxd = 2 * mind
result=multiplyAsDigit(maxd)
while result <= M:
    #探索範囲を広げる
    searching_mind=maxd
    maxd *= 2
    result = multiplyAsDigit(maxd)
    
#print(searching_mind, maxd)
searching_maxd=maxd
while True:
    if searching_maxd - searching_mind <= 1:
        print(searching_maxd - mind)
        exit()
    #探索範囲を狭める
    searching_point = (searching_maxd + searching_mind) // 2
    if multiplyAsDigit(searching_point) > M:
        searching_maxd = searching_point
    else:
        searching_mind = searching_point 
    
    #print(searching_maxd,searching_mind)
    