N = int(input())
A=list(map(int,input().split()))
max_A = max(A)
gcd_degree_of_nums=dict(zip([i+1 for i in range(1,max_A)],[0 for i in range(1,max_A)]))
 
#自身を加えておく
for a in A:
  gcd_degree_of_nums[a]+=1
 
for a in A:
  #約数チェックならその数の半分まで見ればいい
  for div_num in range(2,a//2+1):
    if a % div_num == 0:
      gcd_degree_of_nums[div_num] += 1

max_gcd_degree_of_key =2
max_gcd_degree_of_value =0
for k,v in gcd_degree_of_nums.items():
	if v>max_gcd_degree_of_value:
		max_gcd_degree_of_key =k
		max_gcd_degree_of_value =v

#print(gcd_degree_of_nums)
print(max_gcd_degree_of_key)