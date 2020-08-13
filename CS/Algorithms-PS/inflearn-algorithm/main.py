# 가장 낮은 곳에서 -> 높은 곳으로
#경로 출력 
#더 높은 곳만 갈 수 있음 

def dfs(x,y):
    global mat, cnt, ck 
    ck[x][y] = 1
    
    if x == dest[0] and y == dest[1]:
        cnt += 1
        return 
    
    else:
        #now = (x,y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0<=new_x<(n) and 0<=new_y<(n) and ck[new_x][new_y]==0: #범위에 맞고 
                if mat[new_x][new_y] > mat[x][y]:
                    dfs(new_x, new_y)
                    ck[new_x][new_y] = 0

                

if __name__ == "__main__":
    #init
    start =(0,0)
    dest = (0,0)
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    
    #input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    ck = [[0] * n for _ in range(n)]
    

    #start, dest값 찾기 
    for i in range(n):
        for j in range(n):
            if mat[start[0]][start[1]] > mat[i][j]:
                start = (i,j)
            if mat[dest[0]][dest[1]] < mat[i][j]:
                dest = (i,j)
                
    ck[start[0]][start[1]] = 1
    #op
    dfs(start[0],start[1])
    
    #print()
    print(cnt)


    
    
    
        