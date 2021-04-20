
import sys
input = sys.stdin.readline

dp = [ [[0,0,0], 0] for _ in range(10000+3)]
dp[0] = [[0,0,0], 0] #+1, +2, +3 
dp[1] = [[1,0,0], 1]
dp[2] = [[0,1,0], 1]
dp[3] = [[1,1,1], 3]

for i in range(4, len(dp)):
    tmp = [0,0,0]
    total = 0 

    tmp[0] = dp[i-1][0][1] + dp[i-1][0][2]
    tmp[1] = dp[i-2][0][0] + dp[i-2][0][2]    
    tmp[2] = dp[i-3][0][0] + dp[i-3][0][1]
    
    total = sum(tmp)%1000000009
    dp[i] = [tmp, total]
    
    # print(i,'----', dp[i])
    # cnt += 1
    # if cnt == 10:
    #     break
        

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][1])
    
    
    


