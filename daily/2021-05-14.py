N = int(input())  # 3~10**5

Nodes = [i for i in N]
for _ in range(N):
    a, b = map(int, input().split())
    Nodes[a-1].append[b-1]
    Nodes[b-1].append[a-1]


# 課題:最長となる閉路を見つける
# ->グラフ内で最長となる経路を探せば良い，ってコト...!?
# -> 最長経路探索は難しいらしい→全探索？(N**2)
# あるノードからターゲットへの最長経路がすでにわかっていれば，追加計算をする必要はナッシング
# ->それまでの計算を全てメモしておく
