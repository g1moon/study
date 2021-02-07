# https://www.acmicpc.net/problem/14501
# boj 14501 S4 퇴사 
# <메모리 : 121220, 시간 100>
'''
문제 요약
- 인덱스 두개로 맨뒤부터 하나 하나 앞 수와 비교해 -> 뒤에있는 수가 크면 바꿔주고
- 그 이후로 오름차순 정렬 
'''
n = int(input())
tlst, plst = [], []
res = 0
dp = [0] * (n+1)
for _ in range(n):
    t, p = map(int, input().split())
    tlst.append(t)
    plst.append(p)

mx = 0
for i in range(n-1, 0-1, -1):
    t, p = tlst[i], plst[i]
    #이번 거 할 수 있는지  
    if i+t < len(tlst)+1:
        #오늘 거 하고 + 오늘 작업 끝나고 최대 
        a = plst[i] + dp[i+t]
        #오늘 안 하고 -> 이후 중 최대 
        b = mx 
        dp[i] = max(a, b)    
        mx = max(dp[i], mx)
    else:
        dp[i] = mx
     
print(max(dp))