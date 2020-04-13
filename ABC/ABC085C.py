import cProfile 
def canPayWith(_osatu_array,nokori_pay,nokori_maisu):
    #終了判定
    #払いきれてない
    if len(_osatu_array) == 0 and nokori_pay > 0:
        return False
    #支払い済み
    if len(_osatu_array) == 0 and nokori_pay==0:
        return [0]
    if len(_osatu_array) == 1:
        #ピッタリ払える
        #print("{},{},{}".format(nokori_pay,_osatu_array[0],nokori_maisu))
        if (nokori_pay == _osatu_array[0] * nokori_maisu):
            return [nokori_maisu]
        return False
            

    maxdivide = nokori_pay//_osatu_array[0]
    for i in range(0,maxdivide+1)[::-1]:
        returnArray=canPayWith(
            _osatu_array[1:],
            nokori_pay - i * _osatu_array[0],
            nokori_maisu - i
            )
        if (returnArray == False):continue
        return [i]+returnArray
    
    return False
def main():
    [N,Y]=[int(inp) for inp in input().split()]

    maisu=[]
    osatu_array=[10000,5000,1000]


    maisu=canPayWith(osatu_array,Y,N)
    #ココまでreturn出来てないなら復活不能
    #1050年地下行き
    if maisu == False:
        maisu=[-1 for i in range(len(osatu_array))]

    print(' '.join(map(str, maisu)))

if __name__ == '__main__':
    main()