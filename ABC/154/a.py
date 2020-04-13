[S,T]=[item for item in input().split()]
[A,B]=[int(item)for item in input().split()]
U=input()

if U == S:
    A -= 1
elif U == T:
    B -= 1
print(A,B)