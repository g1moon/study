# sec6 - 인접행렬(가중치 방향 그래프)
#첫쨰 줄에는 정점의 수(N)과 간선의 수 (M)
#다음 M줄에서 (연결정보, 거리비용 )

N,M = map(int, input().split())
g = [[0] * (N+1) for _ in range(N+1)] # 하나 더 여유있게 만들어주고 
for i in range(M):
    a, b, w = map(int, input().split())
    g[a][b] = w
    
#print
for row in range(1, N+1):
    for col in range(1, N+1):
        print(g[row][col], end = ' ')
    print() #한 행을 다 출력하고 -> 줄넘김