def countOnly50Pattern(X,C):
    #valは50の倍数
    return 1 if X/50<=C else 0 

def count100And50Pattern(X, B, C):
    count=0
    for b in range(B+1):
        #print(X,b,C)
        if X - 100 * b >= 0:
            #print("ok")
            count+=countOnly50Pattern(X-100*b,C)
        else:
            #print("ng")
            return count
    return count

def countAllPattern(X,A, B, C):
    count=0
    for a in range(A+1):
        #print(X,a,B,C)
        if X - 500 * a >= 0:
            #print("ok")
            count+=count100And50Pattern(X-500*a,B,C)
        else:
            #print("ng")
            return count
    return count

A=int(input()) 
B=int(input())
C=int(input())
X=int(input())

print(countAllPattern(X,A,B,C))
