import math
[A,B]=[int(item) for item in input().split()]

#Aから判断される、元値として適切な値は?
Akagen=math.ceil(A*12.5 )
Azyogen=math.ceil((A+1)*12.5-1)
#B
Bkagen=math.ceil(B*10 )
Bzyogen=math.ceil((B+1)*10-1 )

#print("{} {} {} {} ".format(Akagen,Azyogen,Bkagen,Bzyogen))
if Azyogen<Bkagen or Bzyogen<Akagen:
    print("-1")
    exit()
print(Akagen if Akagen>Bkagen else Bkagen)