N,A,B=[int(item)for item in input().split()]
S=input()
for c in S:
    if c == 'c':
        print("No")
    elif c == 'a':
        if A == 0:
            if B>0:
                B -= 1
                print("Yes")
            else:
                print("No")
        else :
            A-=1
            print("Yes")
    else:
        #b
        if B == 0:
            print("No")
        else:
            B-=1
            print("Yes")