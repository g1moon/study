# https://www.acmicpc.net/problem/9465
# boj 9465 S2 스티커 
# <메모리 : 185980, 시간 : 340 >
'''
- 현재에서 max(대각선에서 온 것, 2개 컬럼 전 최대 값)
    -> 즉 dp[row][col] = max(dp[0][col-2], dp[1][col-2], dp[1][col-1]) + mat[row][col]        
'''
import sys 
input = sys.stdin.readline

def init_dp(n, mat):
    #return dp table 
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = mat[0][0]
    dp[1][0] = mat[1][0]
    dp[0][1] = mat[0][1] + mat[1][0]
    dp[1][1] = mat[1][1] + mat[0][0]
    return dp

def solution(n, mat):
    dp = init_dp(n, mat)
    res = -1
    for col in range(2, n):
        for row in range(2):
            if row == 0:
                dp[row][col] = max(dp[0][col-2], dp[1][col-2], dp[1][col-1]) + mat[row][col]        
            else: #row == 1
                dp[row][col] = max(dp[0][col-2], dp[1][col-2], dp[0][col-1]) + mat[row][col]
                
    res = max(dp[0][col], dp[1][col])
    return res

#--------------------------
t = int(input())
for _ in range(t):
    n = int(input())
    mat = []
    for _ in range(2):
        mat.append(list(map(int,input().split())))
    print(solution(n, mat))
        
