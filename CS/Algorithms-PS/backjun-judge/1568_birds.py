# 1568번: 새 
# https://www.acmicpc.net/problem/1568

#k마리의 새가 나무에 있고 
#1부터 모든 자연수를 오름차순 노래
#k를 노래할 때, k마리의 새가 나무에서 하늘로 날라 
#만약 현재 남아있는 새의수가 k 보다 작을 때 -> 

# 14 -1
# 13 -2
# 11 -3
# 8  -4
# 4  -5,-1  #비빅
# 3 -2
# 1 -3, -1 #삐빅 
# 0

k = int(input())
# k = 14

sec = 0
i = 1
while True:
    if k == 0:
        break

    #크거나 같게 만들어주는 거 주의
    if k >= i: 
        k = k - i
        i += 1
        sec += 1
    else:
        i = 1

print(sec)
