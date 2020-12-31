from collections import defaultdict
N = int(input())
dic=defaultdict(int)
for i in range(N):
  key=input()
  dic[key] += 1

print("AC x {}".format(dic["AC"]))
print("WA x {}".format(dic["WA"]))
print("TLE x {}".format(dic["TLE"]))
print("RE x {}".format(dic["RE"]))