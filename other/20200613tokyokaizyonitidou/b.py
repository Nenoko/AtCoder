A,V=map(int,input().split())
B,W=map(int,input().split())
T = int(input())

#逃げるほうが早い
if V <= W:
  print('NO')
  exit()
else:
  soutaikyori=abs(A-B)
  soutaiV=V-W
  #距離を詰めきれない
  if soutaikyori / soutaiV > T:
    print("NO")
    exit()
  else:
    print("YES")
    exit()
  #距離を詰めきれる?
    #割り切れる
    """
    print("YES")
    exit()
    if soutaikyori%soutaiV==0:
      print("YES")
    else:
      #割り切れない
      amari = soutaikyori % soutaiV
      keikazikan = soutaikyori / soutaiV
      nokorizikan = T - keikazikan
      if A > B:
        A += V * keikazikan
        B += W * keikazikan
      else:
        A -= V * keikazikan
        B -= W * keikazikan

      for t in range(nokorizikan):
        #Aは近づく，Bは離れる
        if A == B:
          print("YES")
          exit()
        elif A > B:
          A -= V
          B -= W
        else:
          A += V
          B += W
      
      print("NO")
    """