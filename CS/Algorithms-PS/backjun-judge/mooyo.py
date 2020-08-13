#16768: Mooyo Mooyo
#https://www.acmicpc.net/problem/16768

#n =row // c = 10 
#0은 empty 1~9는 컬러 
def new_arr(N):
    ret = [[False for i in range(10)] for _ in range(N)]
    return ret

N, K = map(int, input().split())
M = [list(map(int,list(input()))) for i in range(N)]
dx, dy = [0,1,0,-1], [1,0,-1,0]
ck1, ck2 = new_arr(N) , new_arr(N)



def dfs(x,y):
    global M 
    ck[x][y] = True #그룹에 있는가 
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx <0 or xx >=N or yy < 0 or yy >=10:
            continue
        #만약 그 값들이 다르다면 -> 다른 것임 -> 같은 숫자인 애들만 연결하는데
        #지금 있는 것과 다음으로 갈 것이 다르다면 -> 연결이 되지 않음
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        
        ret += dfs(xx,yy)
    return ret
        
def dfs2(x,y,val):
    global M 
    global dx, dy
    ck2[x][y] = True
    M[x][y] = 0 #################
    for i in range(4):
        xx, yy = x + dx[i], y + dx[i]
        
        if xx<0 or xx>=N or yy<0 or yy >= 10:
            continue
        
        if ck2[xx][yy] or M[xx][yy] != val:
            continue 

def down(M):
    for c in range(10):
        tmp = []
        for r in range(N):
            if M[r][c] != 0:
                tmp.append(M[r][c])
        
        for rr in range(N):
            if rr >= (N- len(tmp)):
                M[rr][c] = tmp.pop(0)
            else:
                M[rr][c] = 0

###########main()###################################
while True:
    exist = False
    ck = new_arr(N)
    ck2 = new_arr(N)
    
    for i in range(N):
        for j in range(10):
            if M[i][j] == 0 or ck[i][j] == True:
                continue
            res = dfs(i,j) #개수 새기
            if res >= K:
                dfs2(i,j,M[i][j]) #지우기
                exist = True
    
    if not exist:
        break
    
    down(M) #내리기
    
##
ret_lst = [] 
for i in M:
    ret_lst.append(list(map(str, i)))
    
for i in ret_lst:
    print(''.join(i))