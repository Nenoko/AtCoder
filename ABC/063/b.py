S=input()
isExist=[False for i in range(26)]
for s in S:
    index=ord(s)-ord('a')
    if isExist[index]:
        print("no")
        exit()
    else:
        isExist[index]=True
print('yes')