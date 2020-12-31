S=input()
T=int(input())

question_cnt=0
drone_x=0
drone_y=0

for s in S:
  if s == '?':
    question_cnt+=1
  elif s == 'L':
    drone_x-=1
  elif s == 'R':
    drone_x+=1
  elif s == 'U':
    drone_y+=1
  elif s == 'D':
    drone_y-=1

#print(drone_x,drone_y,question_cnt)

#ドローンが移動しうる"余地"はquestion_cntに等しい
manhattan_distance = abs(drone_x) + abs(drone_y)
if T == 1:
  #足すだけ
  print(manhattan_distance+question_cnt)
  

elif T == 2:
   if question_cnt <= manhattan_distance:
    print(manhattan_distance-question_cnt)
   else:
    print((-manhattan_distance+question_cnt)%2)