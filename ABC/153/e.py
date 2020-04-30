H,N=[int(i)for i in input().split()]
current_min_c = 0
current_power=0
for i in range(N):
  p,c=[int(i)for i in input().split()]
  current_min_c = current_min_c + c if 