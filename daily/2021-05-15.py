
N = int(input())  # 3~10**5

Edges = [set() for i in range(N)]
# EdgeはN-1本
for _ in range(N-1):
    a, b = map(int, input().split())
    Edges[a-1].add(b-1)
    Edges[b-1].add(a-1)

# 課題:最長となる閉路を見つける
# ->グラフ内で最長となる経路を探せば良い，ってコト...!?
# -> 最長経路探索は難しいらしい→全探索？(N**2)
# あるノードからターゲットへの最長経路がすでにわかっていれば，追加計算をする必要はナッシング
# ->それまでの計算をN**2の配列で保存しておく

# Tは連結で，N-1本の辺がある -> Tは木である -> Tの任意の2点を結ぶ道がちょうど１つある
# よってあるノードと別のノードを結ぶ道は1本しかない

# ...と考えたところで，「木の直径」という概念を発見した
# 木の内部の最長経路は以下のアルゴリズムで求められる :
# 1. あるノードからの最長ノードを求める
# 2. 最長ノードからの最長ノードを求める
# TLEになったのでsetを使う
# 原因は先頭のN^2の配列生成でした...g

tmp_nodes = Edges[0]

# 1. あるノードからの最長ノードを求める
accessed = set([0])
next_edges = set([-1])
longest_node = 0
while not len(next_edges) == 0:
    next_edges = set()
    for n in tmp_nodes:
        if n in accessed:
            continue
        longest_node = n
        accessed.add(n)
        # SetにListを足すときは和集合を作る
        next_edges |= set(Edges[n])
    if len(next_edges) == 0:
        break
    tmp_nodes = next_edges

step = 1
# 2. 最長ノードからの最長ノードを求める

accessed = set([longest_node])
next_edges = set([-1])
tmp_nodes = set(Edges[longest_node])
while not len(next_edges) == 0:
    next_edges = set()
    for n in tmp_nodes:
        if n in accessed:
            continue
        accessed.add(n)
        # SetにListを足すときは和集合を作る
        next_edges |= set(Edges[n])
    if len(next_edges) == 0:
        break
    tmp_nodes = next_edges
    step += 1

print(step)


# def search_next_nodes(cnt, start, tmp_nodes):
#
#    next_nodes = []
#    cnt += 1
#    global memory
#    for n in tmp_nodes:
#        big = -1
#        small = -1
#        if start < n:
#            small = start
#            big = n
#        else:
#            small = n
#            end = start
#        if memory[small][big] == -1:
#            memory[small][big] = cnt
#            next_nodes.extend(Edges[n])

#tmp_max_distance = 0
# for i, start_n in enumerate(N):
#    # 再帰で幅優先探索
#    next_nodes = Edges[i]
#    tmp_dist = search_next_nodes(tmp_cnt, next_nodes)
#    if tmp_max_distance < tmp_dist:
#        tmp_max_distance = tmp_dist
#
# print(tmp_max_distance)
