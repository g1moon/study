
#input()
mat=[list(map(int, input().split())) for _ in range(7)]

#init
dist = [[0] * 7 for _ in range(7)]
queue = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

start = (0,0) #now0,0으로 잡고
queue.append(start) #큐에추가 
found = False 

while queue:
    now = queue.pop(0) #1.now잡고 
    for i in range(4): #2.방향4개보고 
        x = now[0] + dx[i] 
        y = now[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and mat[x][y] ==0: #3.범위확인하고
            mat[x][y] = 1 #4.체크해주고
            dist[x][y] = dist[now[0]] [now[1]] + 1 #5.갱신해주고 
            queue.append((x,y)) #6. queue에 넣어주고 

print(dist[6][6])
    
