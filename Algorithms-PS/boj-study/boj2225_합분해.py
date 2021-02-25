# https://www.acmicpc.net/problem/2225
# boj 2225 G5 합분해 
# <메모리 : 123320, 시간 : 124 >
'''
- dp[2][3] : 2번 더해서 숫자 3만들기 
- dp[row][3] =   dp[row-1][3-0] + 0
                 dp[row-1][3-1] + 1
                 dp[row-1][3-2] + 2 
                 dp[row-1][3-3] + 3
- 한번 덜 사용해서 만든 거에 수 하나씩 더해줄 수 있음 
'''

def init_dp(dp):
    #1번더해서 숫자 N은 모두 1 -> 3이면 3, 10이면 10
    for i in range(n+1):
        dp[1][i] = 1
    #k번더해서 숫자 0은 -> 모두 1 -> 0+0+0(3번 더해서 0만들기)
    for i in range(1,k+1):
        dp[i][0] = 1
    return dp

def solution(n, k):
    dp = [[0] * (n+1) for _ in range(k+1)]
    dp = init_dp(dp)
    
    for row in range(2, k+1): #ㄱ
        for col in range(1, n+1): #col -> 만들 숫자
            tmp = 0 
            for i in range(col+1):
                tmp += dp[row-1][col-i]
            dp[row][col] = tmp % 1000000000
        
    return dp[-1][-1]
    
#--------------
import sys 
input = sys.stdin.readline
n, k = map(int, input().split())
res = 0

print(solution(n, k))
