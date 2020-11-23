# boj 9095
# Adding 1s, 2s, and 3s 
import sys 
In = sys.stdin.readline
t = int(In())
n_lst = [ int(In()) for _ in range(t)]

dp = [0] * (max(n_lst)+1)
#초기화
dp[1] = 1
dp[2] = 2
dp[3] = 4 

for i in range(4, max(n_lst)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for n in n_lst:
    print(dp[n])