import sys
input=sys.stdin.readline

fact = [1]
for i in range(1,8+1):
  fact.append(fact[i-1]*i)


def seq_to_index(seq):
  #print?g()
  seq_len=len(seq)
  unused_val=[i+1 for i in range(seq_len)]
  index=0
  for i in range(seq_len):
  #for i in reversed(range(0,seq_len)):
    ##print?g(i)
    #先頭の数字*それまでに通過してきた組み合わせ
    coeff = seq[i]
    coeff_index_in_unused = unused_val.index(coeff)
    index+=coeff_index_in_unused*fact[seq_len-1-i]
    #使用済みの数は削除
    #print?g(coeff,
    #unused_val,
    #coeff_index_in_unused,
    #index,
    #fact[seq_len - 1 - i])

    unused_val.remove(coeff)

  #print?g()
  return index
    
n=input()

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

pindex=seq_to_index(P)
qindex=seq_to_index(Q)

#print?g(pindex)
#print?g(qindex)

print(qindex-pindex if qindex>pindex else pindex-qindex)