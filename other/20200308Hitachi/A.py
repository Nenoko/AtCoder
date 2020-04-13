import re
strin=input()
pattern = '(hi)+$'
if re.match(pattern, strin):
    print("Yes")
else:
    print("No")
