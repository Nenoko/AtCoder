S=input()

for i,c in enumerate(S):
    if i%2==0:
        if not c==c.lower():
            print("No")
            exit()
    else:
        if not c==c.upper():
            print("No")
            exit()

print("Yes")