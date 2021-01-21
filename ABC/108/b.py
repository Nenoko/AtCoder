import math
x1,y1,x2,y2=map(int,input().split())

root2=1.4141356

#中央の点を求める
aDash=x2-x1
bDash=y2-y1

#print('aDash,bDash = {},{}'.format(aDash,bDash))

chuoux=(aDash-bDash)/2
chuouy=(aDash+bDash)/2

#print("chuoux,chuouy={},{}".format(chuoux,chuouy))

chuoux+=x1
chuouy+=y1

#print("chuoux,chuouy={},{}".format(chuoux,chuouy))

#x2を中央揃えする
x2 -= chuoux
y2 -= chuouy

#90度回転
x3= -y2
y3 = x2

#90度回転
x4= -y3
y4 = x3

x2+=chuoux
x3+=chuoux
x4+=chuoux

y2+=chuouy
y3+=chuouy
y4+=chuouy
x3,x4,y3,y4 = [int(i) for i in [x3,x4,y3,y4]]
print(x3,y3,x4,y4)
#math.round