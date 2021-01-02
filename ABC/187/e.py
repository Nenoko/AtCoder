class node :
    c=0
    childs=[]
    child_tree_sum={}

N=int(input())
nodes=[node() for _ in range(N)]
for n in N:
    a,b=map(int,input().split())
    nodes[a].childs.append(b)
    nodes[b].childs.append(a)
    