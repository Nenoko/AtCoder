import re
pattern = (
   re.compile(r"^dream.*$"),
   re.compile( r"^dreamer.*$"),
   re.compile( r"^erase.*$"),
   re.compile(r"^eraser.*$")
)
base=("dream","dreamer","erase","eraser")
baselen = {patternitem:len(baseitem) for patternitem,baseitem in zip(pattern,base)}

kouho=[]

#SUCCESS="SUCCESS!!"
#FAILURE="FAILURE......"
SUCCESS="YES"
FAILURE="NO"

def patternMatcher(stri):
    #とりあえずいっぺん回す
    for pat in pattern:
        if pat.match(stri):
            #print(stri[baselen[i]:])
            kouho.append(stri[baselen[pat]:])
            if len(stri[baselen[pat] :]) == 0:
                return SUCCESS
    #print(kouho)
    while len(kouho)!=0:
        for kouhoitem in kouho:
            for pat in pattern:
                if pat.match(kouhoitem):
                    #print(stri[baselen[i]:])
                    if len(kouhoitem[baselen[pat] :]) == 0:
                        return SUCCESS
                    kouho.insert(0,kouhoitem[baselen[pat] :])
            #マッチしたか否かに関わらず既存の候補は切る   
            kouho.remove(kouhoitem)
                
    return FAILURE
                

result=patternMatcher(input())
print(result)