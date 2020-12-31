N=int(input())
A=list(map(int,input().split()))

#3
#2 -1 -2

ruisekiwa=[A[0]]
for a in A[1:]:
	ruisekiwa.append(ruisekiwa[-1]+a)
#print(ruisekiwa)
#[2, 1, -1]

prev_all_sum=0
highest_point = 0
tmp_max_ruisekiwa=0
for i in range(0, N):
	#最大和候補
	if ruisekiwa[i]>tmp_max_ruisekiwa:
		tmp_max_ruisekiwa=ruisekiwa[i]
	tmp_max=prev_all_sum
	if(tmp_max_ruisekiwa>0):
		 tmp_max+= tmp_max_ruisekiwa 
	if tmp_max > highest_point:
		highest_point = tmp_max
	prev_all_sum += ruisekiwa[i]
	#print(prev_all_sum)
	
print(highest_point)
