# https://www.acmicpc.net/problem/11659
# boj 11659 S3 (구간합구하기4)
#<메모리 : 136524 / 시간 : 228 > 
'''
- dp : 1부터 idx까지 더한 수 
- 4~10까지 더한 값 = (1~10더한 값) - (1~3더한 값)
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) #개수 n, 합을구해야하는 횟수 m 
lst = list(map(int, input().split()))
dp = [0] * (n+1)



for i in range(1,len(lst)+1):
    dp[i] = dp[i-1] + lst[i-1]
    

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
    
