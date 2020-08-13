'''
- N*N격자판 -> 항상 홀수
- 다이아몬드 모양의 격자판 안에만 수확 -> 격자판 안에 모두 카운트
- 4방향(12시, 3시, 6시, 9시) 으로 나아가면 -> 격자판 모양이 나옴 
    ->n//2 번 나아가면 된다 
'''

#input(mat)--------------
mat = []
n = int(input())
for _ in range(n):
    mat.append(list(map(int, input().split())))
#init---------------------------
#방향 , ck
dx = [-1, 0, 1, 0] #row
dy = [0, 1, 0, -1] #col 
#ck
ck = [[0]* n for _ in range(n)]


#
ret = 0 #격자판 사과 더할 변수 
queue = []

#process----------------------------
queue.append((n//2, n//2))
ck[n//2][n//2] = 1
ret = mat[n//2][n//2]

l = 0 #level
while True:
    if l == n//2:
        break 
    
    size = len(queue) #첫센터 -> 동서남북하면 -> 4개가 새로운 시작점으로 queue에 담김
    #-> 그러면 이 새로운 시작점4개에서 다시 동서남북을 봐야하니까 -> 반복문으로 now를 4번
    for _ in range(size): #1레벨(시작)--------------------------------
        now = queue.pop(0) #처음에 4번 갱신됨 -> 4*4방향(16번 갱신)
        for i in range(4):
            x = now[0] + dx[i]    
            y = now[1] + dy[i]
            if ck[x][y] == 0: 
                nxt = (x,y) 
                ck[nxt[0]] [nxt[1]] = 1 #1.체크 
                queue.append(nxt) #2.추가
                ret += mat[x][y] #3. 더하기 
    l += 1 #1레벨(끝)------------------------------------------------
print(ret)
                
                

