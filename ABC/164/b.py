A,B,C,D=[int(i) for i in input().split()]
aokiAttack=A//D+(A%D>0)
takahashiAttack=C//B+(C%B>0)

print("Yes" if takahashiAttack<= aokiAttack else "No")