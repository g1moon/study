# https://www.acmicpc.net/problem/1309
# boj 1309 S1 동물원 
# <메모리 : 127304, 시간 : 136 >

'''
- 맨 마지막 줄에 사자가 없는 경우, 왼쪽에 있는 경우, 오른쪽에 있는 경우 
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [[1, 1, 1] for i in range(n+2)]

for i in range(2, n+2):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])%9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2])%9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1])%9901

    
print(dp[n+1][0])
    