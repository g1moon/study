# https://www.acmicpc.net/problem/11057
# boj 11057 오르막수
# <메모리: 123352 / 시간: 120>
# 솔루션 
'''
- 길이가 i인 수의 맨 마지막의 앞에가 j인수(0~9)의 관계
- 점화식 : dp[i][j] += dp[i-1][k]
'''
n = int(input())
dp = [[0]*10 for i in range(n+1)]
for i in range(10):
    dp[1][i] = 1
    

for i in range(2, n+1): #2~n
    for j in range(10):
        for k in range(j+1): 
            dp[i][j] += dp[i-1][k]
        
print(sum(dp[-1])%10007)
