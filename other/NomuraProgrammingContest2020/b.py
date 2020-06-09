t=input()
prevc = t[0]
if t[0]!='?':
  newt=t[0]
else:
  newt="D"
for i in range(1,len(t)):
  if t[i] == '?':
    if prevc == 'P':
      newt+='D'
    else:
      newt+='D'
  else:
    newt+=t[i]
  prevc=newt[i]
print(newt)

  