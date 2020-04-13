N = int(input())
kazuof3 = N // 3
kazuof5 = N // 5
kazuof15 = N//15

ans = N * (N + 1) // 2 - kazuof3 * (kazuof3 + 1) * 3 //2 - kazuof5 * (kazuof5 + 1) * 5 // 2 + kazuof15 * (kazuof15 + 1) * 15 // 2
print(ans)