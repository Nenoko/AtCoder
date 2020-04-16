N = input()
S = input()
dic={i:str(i) for i in range(0,10)}
lenS=len(S)
cnt=0
for i in range(0, 1000):
    index=S.find(dic[i // 100])
    if index == -1:
        continue
    elif index + 2 <= lenS:
        index=S.find(dic[(i-(i//100)*100) // 10],index+1)
        if index == -1:
            continue
        elif index+1<=lenS:
            index=S.find(dic[i-(i//10)*10],index+1)
            if index != -1 and index < lenS:
                #print("{}".format(i))
                cnt+=1
print(cnt)