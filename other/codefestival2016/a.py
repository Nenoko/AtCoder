S = input()
cnt=0
for i,c in enumerate("CODEFESTIVAL2016"):
    cnt+=S[i]!=c
print(cnt)