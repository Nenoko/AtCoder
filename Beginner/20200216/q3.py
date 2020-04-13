loopcnt = int(input())
dic = {}
for i in range(0, loopcnt):
    tmp = input()
    #print(dic[tmp])
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic_sorted = sorted(dic.items(),key=lambda x:(-x[1],x[0]))
limit = dic_sorted[0][1]
#debug
#print()
for nametpl in dic_sorted:
    if nametpl[1] == limit:
        print(nametpl[0])
    else:
        break
