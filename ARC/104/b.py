l,S = input().split()
counter = 0
s_number=[]
for s in S:
    if s == 'A':
        s_number.append(1)
    elif s == 'T':
        s_number.append(-1)
    elif s == 'G':
        s_number.append(10000)
    elif s == 'C':
        s_number.append(-10000)


for i in range(1,len(S)):
    inloop_cnt=s_number[0]
    for j in range(1, len(s_number)):
        inloop_cnt += s_number[j]
        if inloop_cnt == 0:
            counter+=1
    s_number=s_number[1:]

print(counter)