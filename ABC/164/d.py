def to10sin(listo):
  retval=0
  for i in listo:
    retval*=10
    retval += i
  return retval

#intarray=input()
intarray=[int(i) for i in input()]

nisennzyuukyuuwarikirecnt=0
#print(intarray)
#print(len(intarray))
#先頭
renzokucnt=0
for i in range(0, len(intarray) - 3):
  #ケツ
  tmp = to10sin(intarray[i:i+3])#←あえて一個少なくしている
  #print(tmpsum)
  for j in range(i+3, len(intarray)):
    tmp *= 10
    tmp+=intarray[j]
    if tmp%2019==0 :
      #print(tmp)
      i = j + 1
      renzokucnt+=1
      break
    elif renzokucnt > 0:
      nisennzyuukyuuwarikirecnt+=renzokucnt*(renzokucnt+1)//2
      renzokucnt=0

nisennzyuukyuuwarikirecnt+=renzokucnt*(renzokucnt+1)//2
print(nisennzyuukyuuwarikirecnt)
