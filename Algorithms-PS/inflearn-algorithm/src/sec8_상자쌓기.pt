'''
- 밑면이 정사각형인 직육면체 벽돌들을 사용해 탑을 쌓고자 한다
- 아래에서 위로 쌓으면서 -> 
- 조건을 만족하면서 -> 가장 높은 탑을 쌓을 수 있는 프로그램

- 벽돌은 회전 불가능 (즉 옆면을 밑면으로 할 수 없음)
- 밑면의 넓이가 같은 벽돌 없고, 무게가 같은 벽돌도 없음
- 벽돌들의 높이는 같을 수도 있음
- 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌을 놓을 수 없음
- 무게가 무거운 벽돌을 무게가 가벼운 벽돌위에 올릴 수 없음

-> 다음으로 올게 -> 밑면도 좁아야하고 -> 무게도 가벼워야함
'''

lst = []
n =int(input())#벽돌의 수 #최대 100
for _ in range(n):
    base, height, weight = map(int, input().split())
    lst.append([base, height, weight])

dy = [0] * n
dy[0] = lst[0][1]
# print(lst)
lst.sort(key = lambda x : x[0], reverse = True)
# print(lst)

# for i in range(1, n):
#     dy[i] = lst[i][1]
#     for j in range(i-1, -1, -1):
#         res = lst[i][1]
#         if lst[j][2] > lst[i][2]:
#             res += dy[j]
        
#         dy[i] = max(dy[i], res)
# # print(dy)
# print(max(dy))

res = lst[0][1]
for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if lst[j][2] > lst[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + lst[i][1]
    res = max(res, dy[i])
print(res)            
            
            
        
        
            


