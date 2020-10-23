'''
- N * N
- 높이는 서로 다름
- 해당 돌다리 건널 때 -> 돌의 높이 만큼 에너지 소비 
- 현재 지점에서 (오른쪽, 아래만 이동가능)
- (1,1)에서 (N, N) 까지 가는데 드는 에너지의 최소량

'''

'''
solution
1. arr에서 0행과, 0열은 한쪽 방향으로만 진행가능하기떄문에 -> 쭉 적어줌m 
2. 그리고 이중 포문으로 -> (왼쪽에서 오는 경우, 위에서 오는 경우) 에서 작은 거를 할당
'''

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]
dy[0][0]=arr[0][0]

for i in range(1, n):
    dy[0][i]=dy[0][i-1]+arr[0][i]
    dy[i][0]=dy[i-1][0]+arr[i][0]
for i in range(1, n):
    for j in range(1, n):
        dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
print(dy[n-1][n-1])
