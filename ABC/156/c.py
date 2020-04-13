from statistics import mean
N=int(input())
X=[int(item)for item in input().split()]
meanX = round(mean(X))
print(sum([(X_-meanX)**2 for X_ in X]))