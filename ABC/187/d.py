N = int(input())
ax2_plus_b = []
asum = 0
for _ in range(N):
    a, b = map(int, input().split())
    ax2_plus_b.append(2 * a + b)
    asum -= a

ax2_plus_b = sorted(ax2_plus_b)[::-1]

for i, e in enumerate(ax2_plus_b):
    asum += e
    if asum > 0:
        print(i + 1)
        exit()


# print(asum)
# print(ax2_plus_b)
