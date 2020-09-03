# 구현 - 실전문제3 - 게임 개발

'''
- (N * M) 육지 or 바다
- 동서남북중 한 곳을 바라보고 있음
- 각 칸은 ((A,B)) , a는 북쪽으로 떨어진 칸의 개수 ,b는 왼쪽으로 떨어진 칸의 개수 
- 상하좌우 이동 가능, 바다는 이동 불가능

- 1. 서,남,동,북 순으로 갈 곳을 정한다
- 2. 왼쪽에 아직 가보지 않은 칸 있으면 ->  왼쪽으로 회전하고 한칸 이동
    - 만약 왼쪽을 가봤으면, 왼쪽으로 회전만하고 다시 1단계 
- 3. 1. 동서남북 모두 가보거나 2.바다거나 ->
- 
'''
def turn_left(dir):
    if dir == 0: #북
        return 3
    elif dir == 1:
        return 0
    elif dir == 2:
        return 1
    elif dir == 3:
        return 2
    
def go_fwd(a,b, dir):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    return (a + dx[dir], b + dy[dir], dir)

def go_bwd(a,b, dir):
    #북 동 남 서 
    #남, 서, 북, 동
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    return (a + dx[dir], b + dy[dir], dir)
    
    

#0, 1, 2, 3 
#북 동 남 서 
#dx 서 남 동 북 
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#방문한 곳
cnt = 0

#input()
n, m = map(int, input().split())
a, b, d = map(int, input().split())
mat = []
ck = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
    ck.append([0] * m)
#현재 위치 
cur = (a,b,d)

#시작점 들렸던 곳으로 체크 
ck[a][b] = 1
cnt += 1 #한 곳 방문
print(cur)
stop = False
while True:
    all_around_done = True
    for _ in range(4):
        left_dir = turn_left(cur[2])
        left = go_fwd(cur[0], cur[1], left_dir)

        #조건3개다 만족
        if ck[left[0]][left[1]] == 0:
            if mat[left[0]][left[1]] == 0:
                #왼쪽으로 회전하고
                cur[2] = turn_left(cur[2]) #그럼 방향이 바뀌고
                cur = go_fwd(cur[0], cur[1], cur[2])#앞으로 전진
                ck[cur[0]][cur[1]] = 1 #체크해주고
                cnt += 1 #증가 
                print(cur)
                all_around_done = False
        elif ck[left[0]][left[1]] == 1:
            cur[2] = turn_left(cur[2]) #회전만 
            continue 
    
    if all_around_done:
        cur = go_bwd(cur[0], cur[1], cur[2])
        if ck[cur[0]][cur[1]] == 0:
            cnt += 1
            print(cur)
            ck[cur[0]][cur[1]] = 1
        
        if mat[cur[0]][cur[1]] == 1:
            print(cnt)
            break
        
        continue


        
                
                

    
    
    
    
    
    
    
        # ##4방향 확인-------------------------------
        # done = True
        # for i in range(4):
        #     one_dir = (cur[0] + dx[i], cur[1] + dy[i])
        #     #안가보고, 바다가 아니어야해 
        #     if ck[one_dir[0]][one_dir[1]] == 0:
        #         if mat[one_dir[0]][one_dir[1]] == 0:
        #             done = False
        #             break 
        # if done: #4방향 모두 가보거나, 바다야 
        #     #1. 방향 유지하고 
        #     #2. 한칸 뒤로 
        #     cur = go_bwd(cur[0], cur[1], cur[2])
        #     if mat[cur[0]][cur[1]] == 1:
        #         stop = True
        #         break 
        #     else:
        #         ck[cur[0]][cur[1]] == 0:
        #             cnt += 1
                    
        # if stop:
        #     print(cnt)
        # #-----------------------------------------------