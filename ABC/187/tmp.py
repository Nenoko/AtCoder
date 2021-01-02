S=input()

min_dist=999

for i in range(0,len(S)-2):
	evaluating_num=int(S[i:i+3])
	dist = abs(753-evaluating_num)
	#print(evaluating_num,dist)
	min_dist=min(dist,min_dist)

print(min_dist)