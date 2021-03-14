# https://www.acmicpc.net/problem/3190
# boj 3190 G5 뱀 
# <메모리 : 29380, 시간 : 76 >

'''
- (N * N) 정사각 보드위에서 진행 , 사과가 있는 칸이 있음
- 보드의 상하좌우 끝에는 벽이있음 
- 시작할때 뱀의 좌표는(0,0) -> 뱀길이는1 -> 오른쪽을 향함

- 1. 몸길이를 늘려 머리를 다음칸에 위치함
- 2. 이동한 칸에 사과가 있으면 -> 그 칸의 사과 없어지고 -> 꼬리는 움직이지 않음
- 3. 이동한 칸에 사과가 없으면 -> 몸길이를 줄여 -> 꼬리가 위치한 칸을 비움 (길이변동없음)

input : 사과의 위치와, 뱀의 이동경로
return : 이 게임이 몇 초에 끝나는지 (벽 또는 자기자신의 몸이 닿으면 종료)
'''

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [float('inf') for _ in range(n)]
dp[0] = 1

for i in range(0,n):
    for j in range(i+1, i + lst[i] + 1):
        if j < n:
            dp[j] = min(dp[j], dp[i]+1)
            
if dp[n-1] == float('inf'):
    print(-1)
else:
    print(dp[n-1] - 1)    
    





