#https://www.acmicpc.net/problem/11726
#Boj 11726
#<메모리: 121220 / 시간: 104>
n = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1

for i in range(2, n+1): #2~n
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[n]%10007)

