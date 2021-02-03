# https://www.acmicpc.net/problem/1003
# boj 1003 S3 (피보나치)
#<메모리 : 121220 / 시간 : 104 > 
'''
- fibo(3) 은 fibo(2) 와 fibo(2) 호출 
- fibo(4) 는 fibo(3)과 fibo(2) 호출 
 -> fibo(3) 값과 fibo(2) 값을 참고해 값 계산 
'''

import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 41
dp[0] , dp[1] = (1,0), (0,1)

for i in range(2, len(dp)):
    dp[i]= (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    
for _ in range(t):
    n = int(input())
    print(dp[n][0], end =' ')
    print(dp[n][1])
    
