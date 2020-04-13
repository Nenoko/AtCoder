[N,A,B]=input().split()
#print("{},{},{}".format(N,A,B))
count=0
for i in range(int(N)+1):
    #桁ごとの数字に分けるよ
    ketagoto = [int(stri) for stri in str(i)]
    #足すよ〜ん
    sumketa = sum(ketagoto)
    #調べるよ〜ん^^
    if int(A) <= sumketa and sumketa <= int(B):
        #print(i)
        count+=i
print (count)