# https://www.acmicpc.net/problem/14501
# boj 14501 S4 퇴사 
# <메모리 : 121220, 시간 100>
'''
문제 요약
- 맨 마지막 날 부터 이 날 작업을 할지 안 할지 확인
    -> 작업을 한다면 : plst[i] + dp[i+t] #일하고, 다음 일 가능한 것중 최대 
    -> 안 하면 그냥 이후에서 최대 골라 
'''
n = int(input())
tlst, plst = [], []
res = 0
mx = 0 #뒤에서부터 최대 페이 기록 

dp = [0] * (n+1)
for _ in range(n):
    t, p = map(int, input().split())
    tlst.append(t)
    plst.append(p)


for i in range(n-1, 0-1, -1):
    t, p = tlst[i], plst[i]
   
    #이번 거 할 수 있는지(하고 안 하고 선택가능) 
    if i+t < len(tlst)+1: #1일자에 1일 걸리는 작업이라면 -> 2일자 가능  
        a = plst[i] + dp[i+t] #오늘 거 하고 + 오늘 작업 끝나고 최대 
        b = mx #오늘 안 하고 -> 이후 중 최대  
        dp[i] = max(a, b)    
        mx = max(dp[i], mx)
   
    #무조건 못해 
    else:
        dp[i] = mx
     
print(max(dp))