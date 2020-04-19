N, K = [int(i) for i in input().split()]
cnt=0
for i in range(K,N+2):
    minval=(i-1)*(i)//2
    maxval=i*(N+1)-i*(i+1)//2
    cnt+=maxval-minval+1
    #print("i,max,min,cnt={},{},{},{}".format(i,minval,maxval,cnt))
print(cnt%1000000007)