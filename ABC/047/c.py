def BWstripper(S):
  BWarray=[]
  while (len(S) != 0):
    initial = S[0]
    tmp=""
    while (S[0] == initial):
      tmp+=S[0]
      S=S.lstrip(initial)
      if len(S) == 0:
        break
    BWarray.append(tmp)
  return BWarray
S=input()
stripped = BWstripper(S)
print(len(stripped)-1)