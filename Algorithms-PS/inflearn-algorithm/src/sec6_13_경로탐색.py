#sec6_13_경로탐색_(그래프DFS)
#첫쨰 줄에는 정접의 수 (N) #간선의 수 M
#그 다음 M줄에 걸쳐 연결정보가 

'''
1. 방문하면 체크해줄 것(방문했던 노드라고)
2. for문을 돌면서 자기 자신이라면 -> 컨티뉴 
3. for문 돌면서 방문했던 곳이면 -> 컨티뉴
4. for문 돌면서 현재 node와 연결된 곳이 나오면 (g[node][i]==1) -> dfs(i)
5. for문 다 돌면서 ck[node] = 0 으로 방문점 풀어주기 
'''
def dfs(node):
    global cnt
    if node == N:
        cnt += 1
        ck[node] = 0 #ck풀어주기 
        return 
    
    else:
        ck[node] = 1 # ck
        for i in range(1, N+1): #i를 1~N 까지
            if i == node: continue # 자기 자신은 패스
            if ck[i] == 1: continue # 방문했던 곳이면 패스 
            #이렇게되면 자기자신과, 방문했던 곳은 패스가 되고 
            if g[node][i] == 1: #연결된 곳이면
                dfs(i)
        ck[node] = 0 #for문 다 돌면 ck 풀어주기 
        

if __name__ == "__main__":
    N, M = map(int, input().split())
    g = [[0]*(N+1) for _ in range(N+1)]
    cnt = 0
    ck = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a][b] = 1
    
    dfs(1)
    print(cnt)
    
    
    