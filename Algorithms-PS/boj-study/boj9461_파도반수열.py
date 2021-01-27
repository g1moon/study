#https://www.acmicpc.net/problem/9461
#boj 9461 파도반수열
#<메모리 : 121220 / 시간 : 116>
'''
- lst = [1,1,1,2,2,3,4,5,7,9, ...]
- 위에서 점화식 찾을 수 있음
    -> dp[i] = dp[i-2] + dp[i-3]
'''

lst = [1,1,1,2,2,3,4,5,7,9]
dp = [0] * 101
for i in range(len(lst)):
    dp[i] = lst[i]


for i in range(4, len(dp)):
    dp[i] = dp[i-2] + dp[i-3]
    
t = int(input())
for _ in range(t):
    a = int(input())
    print(dp[a-1])
    
