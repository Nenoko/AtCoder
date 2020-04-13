input()
array = [int(a) for a in input().split()]
counter=0
while True:
    newArray=[]
    for a in array:
        if a % 2 == 0:
            newArray.append(a/2)
        else:
            print(counter)
            exit()
    array=newArray
    counter+=1