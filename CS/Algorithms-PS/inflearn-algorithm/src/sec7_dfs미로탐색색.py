# #x,y가 7,7이면 -> cnt +=1 하고 종료

def dfs(x,y):
    global ck, mat, cnt
    mat[x][y] = 1
    if x == 6 and y == 6:
        cnt += 1
        return

    else:
        for i in range(4):
            nxt_x = x + dx[i]
            nxt_y = y + dy[i]
            if 0<=nxt_x<=6 and 0<=nxt_y<=6 and mat[nxt_x][nxt_y] == 0:
                dfs(nxt_x, nxt_y)
                mat[nxt_x][nxt_y] = 0
                
            
            
    


if __name__ == "__main__":
    #init
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    #input()
    mat = [list(map(int, input().split())) for _ in range(7)]
    ck = [[0] * 7 for _ in range(7)]
    
    dfs(0,0)
    
    print(cnt)
    
    
    
    
    

