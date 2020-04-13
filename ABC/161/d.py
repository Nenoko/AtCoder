class Node:
    parent=-1
    myself=-1
    def __init__(self,parent_,myself_):
        parent=parent_
        myself_=myself_



#木の生成
tree = [[
    Node(-1,1),
    Node(-1,2),
    Node(-1,3),
    Node(-1,4),
    Node(-1,5),
    Node(-1,6),
    Node(-1,7),
    Node(-1,8),
    Node(-1,9)
]]
treesize = len(tree[0])
K = int(input())
if K<10:print(K)
for i in range(114514):
    newbranch=[]
    for item in tree[i]:
        if item.myself == 1:

            newbranch.append(Node(1,0))
            newbranch.append(Node(1, 1))
        elif item.myself ==9: