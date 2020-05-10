N,K=[int(i)for i in input().split()]
A = [int(i) for i in input().split()]

#インデックスを1オリジンに
A.insert(0,-1)

accessed_node = set([1])
accessed_node_list=[1]
loop_root = []
loop_madeno_size = 0
loop_size=0
t=1
#ループ検出
for _ in range(1,K+1):
  if not A[t] in accessed_node:
    accessed_node.add(A[t])
    accessed_node_list.append(A[t])
    #次の場所を決める
    t=A[t]
  else:
    #ループ路を確定する
    loop_start_index=accessed_node_list.index(A[t])
    loop_root = accessed_node_list[loop_start_index:]
    loop_madeno_size = loop_start_index
    loop_size=len(loop_root)
    break
#print(accessed_node)
#print(loop_madeno_size)
if loop_madeno_size <= K:
  print(t)
  exit()
K -= loop_madeno_size
print(loop_root[K%loop_size])
