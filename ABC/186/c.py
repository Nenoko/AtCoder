N = int(input())
cnt=0
for n in range(1, N + 1):
	strn=str(n)
	if '7' in strn:
		continue
	stroctn = str(oct(n))

	if '7' in stroctn:
		continue

	cnt+=1

print(cnt)