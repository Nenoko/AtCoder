list = input().split()
a = list[0]
b = list[1]
c=list[2]

if (a == b or b == c or c == a)and not (a==b and b==c):
    print("Yes")
else:
    print("No")
