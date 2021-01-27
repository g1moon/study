#https://www.acmicpc.net/problem/11726
#boj 11726 2N타일
#<메모리: 121220 / 시간: 104>
'''
- dp = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…..]
- 점화식
    -> dp[i] = dp[i-2] + dp[i-1]
'''

n = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1

for i in range(2, n+1): #2~n
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[n]%10007)

