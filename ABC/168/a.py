#A=[int(i)for i in input().split()]
A=input()
#print(A)
lastnum=int(A[-1])
if lastnum == 3:
  print("bon")
elif lastnum == 0 or lastnum == 1 or lastnum == 6 or lastnum == 8:
  print("pon")
else:
  print("hon")