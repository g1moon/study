#https://www.acmicpc.net/problem/7562
#boj 7562(S2) 나이트의 이동

'''
- 1: 테스트케이스
- 1 : 체스판의 한 변의 길이 (i) 체스판 i*i
- 2 : 나이트 현재 
- 3 : 나이트 이동하려는 칸 
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,cnt):
    global res, ck
    ck[x][y] = 1
    if x == dest_x and y == dest_y:
        print(cnt)
        # if res > cnt: 
        #     res = cnt
        return 
    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx >= 0 and ny >=0 and nx < i and ny < i:
            if ck[nx][ny] == 0:
                dfs(nx,ny, cnt + 1)
                    

t = int(input())
for _ in range(t):
    i = int(input())
    cur_x, cur_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    ck = [ [0] * i for _ in range(i)]
    
    #동서남북으로 이동하는데 -> 범위 넘어가면  return 
    res = 10000000
    ck[cur_x][cur_y] = 1
    dfs(cur_x, cur_y,0)
    # print(res)
    break 