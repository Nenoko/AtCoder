N = int(input())
A = list(map(int, input().split()))

#オーダnlogn
A.sort()

sum_ = 0

sumofsoremade = []
sumofsoremade_=0

#累積和を作る
#オーダn
for a in A:
	sumofsoremade_ += a
	sumofsoremade.append(sumofsoremade_)

#オーダn
for n in reversed(range(1,N)):
	sum_ += A[n]*n - sumofsoremade[n-1]

print(sum_)