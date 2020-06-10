from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())

WAinProblem=defaultdict(int)#defaultdictは初期値が0(int)なdict
totalWA=0
totalAC=0
for _ in range(M):
  line=stdin.readline().split()
  problem_number=int(line[0])
  result=line[1]

  if result == "WA":
    if WAinProblem[problem_number]!=-1:#集計終了していなければ
      WAinProblem[problem_number]+=1
  else:#result="AC"
    if WAinProblem[problem_number]!=-1:#集計終了していなければ
      totalWA+=WAinProblem[problem_number]
      totalAC += 1
      WAinProblem[problem_number]=-1#集計終了
print("{} {}".format(totalAC,totalWA))