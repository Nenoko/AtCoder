from sys import stdin
from math import log10,floor

input=stdin.readline

A,B,X=map(int,input().split())

#Nを買うにはA+N+B+d(N)が必要
##N桁の整数の最大値が購入可能かどうかを先に調べる？
#2分探索にトライしてみる？
  #2分探索なら1000000000に対する探索もたかだか29回で住む

start = 0
end=1000000000

point = end
point_keta = floor(log10(point))+1
val=(A * point + B * point_keta)
#print(val)
if X >= val:
  print(1000000000)
  exit()

while(True):
#for i in range(100):
  if end - start == 1:
    print(start)
    exit()
  point = (start + end) // 2
  point_keta = floor(log10(point))+1
  val=(A * point + B * point_keta)
  if end - start == 2:
    if val > X:  #デカすぎた
      print(start)
      exit()
    else:
      print(point)
      exit()

    
  if val == X:#ピッタリ
    #値段を決定する式自体は強い増加関数なので，イコールになったということはその値が買える限界の値
    print(point)
    exit()
  elif val >X:#デカすぎた
   # print("big",start,point,end,point_keta,val)
    #小さい側に寄せる
    end=point
  else:#手持ち金よりちっせえ
    #print("small", start, point, end,point_keta, val)
    #デカくする
    start=point
  #こんなかんじで2分探索していくゾ〜



#if (A * 1 + B * 1 // 10) > X:
#  print(0)
#  exit()
#for i in range(2,X+1):
#  tmpval=A*i+B*i//10
#  #print("{},{}".format(tmpval,"購入可能"if tmpval<=X else "かえません"))
#  if tmpval > X:
#    print(i-1)
#    exit()
#
#print(X)
#exit()