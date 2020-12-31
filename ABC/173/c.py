def rec_pattern_get(pattern_num,pattern):
  return pattern_num


from collections import Counter

H,W,K=map(int,input().split())
masume = []

for i in range(H):
  masume.append(input())


tf=[]
#ビット全探索
for i in range(2**H):
  tmp=[]
  for j in range(H):
    if ((i >> j) & 1):
      tmp.append(masume[j])
  print(tmp)

  for j in range(2 ** W):
    tmp_tmp=[]*len(tmp)
    for k in range(W):
      if ((j >> k) & 1):
        #列を追加
        for l in range(len(tmp)):
          print(l,k,tmp[l][k])
          tmp_tmp[l].append(tmp[l][k])


    
  

#for i in range(H):
#  print(masume[i])