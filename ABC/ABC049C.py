import re
#dreampat=re.compile(r"^dream")
#erpat=re.compile( r"^er")
#aspat=re.compile( r"^as")
#epat=re.compile(r"^e")
sentouerafterpat=re.compile(r"^eras")
matubierafterpat=re.compile(r"^er(dream|er)")
#gatimatubierpat = re.compile(r"^(dream|as)$")
#gatimatubierpat = re.compile(r"^[02]$")
#sentouerbeforepat = re.compile(r"^(er|e|dream)$")
#sentouerbeforepat = re.compile(r"^[013]$")
#matubierbeforepat=re.compile(r"^(dream|as)")
#matubierbeforepat=re.compile(r"^[02]$")
#base=("dream","er","as","e")
#baselen = {item:len(item) for item in base}


#SUCCESS="SUCCESS!!"
#FAILURE="FAILURE......"
SUCCESS="YES"
FAILURE="NO"

def patternMatcher(stri):
    last=None
    nextislaster = False
    endFlag=False
    while len(stri)>0:
        #if dreampat.match(stri):
        if stri.startswith("dream"):
            ##print("match:dream")
            #dreamの前にあって良いのは、空白、dream、末尾er、eのみ
            #先頭erなら失敗
            if nextislaster and last==1:
                return FAILURE
            #stri=stri[baselen["dream"]:]
            stri=stri[5:]
            last = 0
            #この時点で終了可能
            endFlag=True
            continue
        #if erpat.match(stri):
        if stri.startswith("er"):
            #後ろに何も続いていない場合
            if len(stri)==2:
                ##print("match:finaler")
                #ガチの末尾erと解釈
                #末尾erの前には、dream、asのみ
                #if not(last!=None and re.match(r"^(dream|as)$",last)):
                #if not(last!=None and gatimatubierpat.match(last)):
                if not(last!=None and last==0 or last==2):
                    return FAILURE
                #ここまで来たら成功
                endFlag=True
                return SUCCESS

            #後ろにまだなにか続いている場合
            #これは先頭のerか？末尾のerか？
            #erとそれ以前のフレーズから得られる情報だけでは、これが末尾のerか、先頭のerかを特定することは出来ない
            #これを特定するには、一つ後のフレーズを見る
            #一つ後のフレーズが
            #aseなら先頭er
            #dream、erなら末尾er
            #それ以外はありえないのでFAILURE  
            if last=="e":
                return FAILURE
            #先頭erの前には、空白、末尾er、e,dreamのみ
            if sentouerafterpat.match(stri) or last==None:
                ##print("match:sentouer")
                #if not last==None and not re.match(r"^(er|e|dream)$",last):
                if last!=None and last!=0 and last!=1 and last!=3:
                    return FAILURE
                nextislaster=True
                #この時点で終了不能
                endFlag=False
            elif matubierafterpat.match(stri):
                ##print("match:laster")
                    #末尾erの前には、dream、asのみ
                #if not re.match(r"^(dream|as)",last):
                #if not matubierbeforepat.match(last):
                if last!=0 and last!=2:
                    return FAILURE
                nextislaster=False
                #この時点で終了可能
                endFlag=True
            #共通処理
            stri=stri[2:]
            last=1
            continue

        #if aspat.match(stri):
        if stri.startswith("as"):
            ##print("match:as")
            #asの前には、先頭erのみ
            if last != 1 or nextislaster != True:
                return False
            stri=stri[2:]
            last=2
            #この時点で終了不能
            endFlag=False
            continue

        #if epat.match(stri):
        if stri.startswith("e"):
            ##print("match:e")
            #eの前には、asのみ
            if last != 2:
                return FAILURE
            stri=stri[1:]
            last=3
            #eを通ったということは、次に来るerは必ず先頭erになる
            nextislaster=False
            #この時点で終了可能
            endFlag=True
            continue
        #ここまで来たということは、何もマッチングしなかったということ
        return FAILURE
    #ここに来たということは、striの長さが0になったということ
    if endFlag==True:return SUCCESS
    #先頭erで終わっている場合はヤバい
    else:return FAILURE

    


result=patternMatcher(input())
print(result)