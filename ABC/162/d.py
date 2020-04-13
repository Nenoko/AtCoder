N=int(input())
S = input()
sum=0
for i in range(0, N - 2):
    a = S[i]
    if a == 'R':
        index=S.find('B',i+1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('G')
            if 2*j-i<N and(S[2 * j - i] == 'G'):
                sum -= 1
            if j==N-1:break
            index=S.find('B',j+1)
        index = S.find('G', i+ 1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('B')
            if 2*j-i<N and(S[2 * j - i] == 'B'):
                sum-=1
            if j==N-1:break
            index = S.find('G', j+ 1)
    elif a == 'G':
        index=S.find('B',i+1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('R')
            if 2*j-i<N and(S[2 * j - i] == 'R'):
                sum-=1
            if j==N-1:break
            index=S.find('B',j+1)
        index=S.find('R',i+1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('B')
            if 2*j-i<N and(S[2 * j - i] == 'B'):
                sum-=1
            if j==N-1:break
            index=S.find('R',j+1)
    else:
        index=S.find('R',i+1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('G')
            if 2*j-i<N and(S[2 * j - i] == 'G'):
                sum-=1
            if j==N-1:break
            index=S.find('R',j+1)
        index=S.find('G',i+1)
        while(index!=-1):
            j=index
            sum += S[j + 1 :].count('R')
            if 2*j-i<N and(S[2 * j - i] == 'R'):
                sum-=1
            if j==N-1:break
            index=S.find('G',j+1)
        #    if a!=S[j]:
        #        b=S[j]
        #        if a=='R' and b == 'G' or a=='G' and b=='R':
        #            sum += S[j + 1 :].count('B')
        #            if 2*j-i<N and(S[2 * j - i] == 'B'):
        #                sum-=1
        #        elif a == 'G' and b == 'B' or a == 'B' and b == 'G':
        #            sum += S[j + 1 :].count('R')
        #            if 2*j-i<N and(S[2 * j - i] == 'R'):
        #                sum-=1
        #        else:
        #            sum += S[j + 1 :].count('G')
        #            if 2*j-i<N and(S[2 * j - i] == 'G'):
        #                sum-=1
print(sum)