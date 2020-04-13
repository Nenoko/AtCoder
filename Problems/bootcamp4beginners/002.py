from statistics import mean
import math
N=int(input())
X = [int(item) for item in input().split()]
meanX=mean(X)
underX = math.floor(meanX)
upperX = math.ceil(meanX)

underX=sum([(item-underX)**2 for item in X])
upperX=sum([(item-upperX)**2 for item in X])
print(underX if underX<upperX else upperX)