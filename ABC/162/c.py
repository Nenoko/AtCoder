from  math import gcd
dic = {}
K = int(input())
sum_=0
for a in range(1,K+1):
    for b in range(a,K+1):
        for c in range(b,K+1):
            if a == b and b == c:
                sum_ += gcd(gcd(a, b),c)
            elif a == b or b == c or c == a:
                sum_ += gcd(gcd(a, b),c)*3
            else:
                sum_ += gcd(gcd(a, b),c)*6
print(sum_)