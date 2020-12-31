from collections import Counter
inp=input()
N=Counter([int(s)%3 for s in inp])
criterion = N[1]+N[2]*2
least_del_num=0
if(criterion%3==0):
	least_del_num=0
#1余る
elif(criterion%3==1):
	if N[1]>0:
		least_del_num=1
	elif N[2]>1:
		least_del_num=2
	else:
		least_del_num=-1
else:
	if N[2]>0:
		least_del_num=1
	elif N[1]>1:
		least_del_num=2
	else:
		least_del_num=-1
if len(inp)<=least_del_num:
	least_del_num=-1
print(least_del_num)
