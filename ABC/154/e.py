N = int(input())
splitN=[]
K = int(input())

def cmb(N, K):
    over = 1
    under=1
    for i in range(0,K):
        over *= (N - i)
        under*=(i+1)
    return over/under

#一番トップが埋まっていない想定
total = 9 ** K * cmb(N - 1, K)

