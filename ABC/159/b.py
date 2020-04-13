def iskaibun(s):
    lens=len(s)
    #print(s)
    for i in range(lens // 2):
        #print("{} {}".format(s[i],s[lens-1-i]))
        if s[i] != s[lens-1 - i]:
            return False
    
    return True
    
s = input()
lens=len(s)
#print(s[0: (lens - 2) // 2+1])
#print(s[(lens + 2) // 2 : lens])
if iskaibun(s) and iskaibun(s[0: (lens - 1) // 2]) and iskaibun(s[(lens + 2) // 2 : lens]):
    print("Yes")
else:
    print("No")