input()
passport = input().split()
approveflag=True
for strx in passport:
    x = int(strx)
    if x%2==0 and not (x%3==0 or x%5==0):
        approveflag = False

if approveflag == True:
    print('APPROVED')
else:
    print('DENIED')