N = int(input())
array=[]
for i in range(0, N-1):
    array.append(input().split())
dist3=[]
for row in array:
    a,b=row
    c = []
    d=[]
    for tmpc1,tmpc2 in array:
        if tmpc1 == a and tmpc2 != a and tmpc2!=b:
            c.append(int(tmpc2)-1)
        if tmpc1 != a and tmpc2 == a and tmpc1 != b:
            c.append(int(tmpc1)-1)
    for tmpd1,tmpd2 in array:
        if tmpd1 == b and tmpd2!=a and tmpd2 != b and tmpd2!=c:
            d.append(int(tmpd2)-1)
        if tmpd1 != b and tmpd1!=a and tmpd2 == b and tmpd1!=c:
            d.append(int(tmpd1)-1)
    if c != [] and d != []:
        #print("{} {} {} {}".format(a, b, c, d))
        dist3.append([c, d])
        
for kouho in itertools.permutations(list(range(1,N+1)),N):
    breakflag=False
    for c, d in dist3:
        for tmpc in c:
            for tmpd in d:
                if (kouho[tmpc] + kouho[tmpd]) % 3 != 0 and (kouho[tmpc] * kouho[tmpd]) % 3 != 0:
                    breakflag = True
                    break
                else:
                    print("{} {} {} {}".format( tmpc, tmpd,kouho[tmpc],kouho[tmpd]))
            if breakflag==True:
                break
        if breakflag!=True:
            print(' '.join(map(str,kouho)))
            exit()

print('-1')


//ビーム輝くフラッシュバックにヤツの影
char charchar