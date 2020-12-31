S=input()
T=input()
cnt_min=1001
for i in range(len(S)-len(T)+1):
  #部分文字列を切り出す
  s=S[i:i+len(T)]
  cnt=0
  for i,s_ in enumerate(s):
    if T[i] != s_:
      cnt+=1
  if cnt_min > cnt:
    cnt_min = cnt

print(cnt_min)